from database import get_engine, init_db
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
from sqlalchemy import text
import os
import json

load_dotenv()

engine = get_engine()
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

CHUNK_SIZE = 512  # characters per chunk


def chunk_text(text_data: str) -> list[str]:
    """Split text into overlapping chunks for better context retrieval."""
    words = text_data.split()
    chunks = []
    chunk_words = CHUNK_SIZE // 6  # rough words per chunk

    for i in range(0, len(words), chunk_words):
        chunk = " ".join(words[i: i + chunk_words])
        if chunk.strip():
            chunks.append(chunk)

    return chunks if chunks else [text_data]


def store_data(df, progress_callback=None):
    """
    Embed and store all rows from a DataFrame.
    progress_callback(current, total) is called after each row if provided.
    """
    init_db()

    rows_data = []
    total = len(df)

    for i, (_, row) in enumerate(df.iterrows()):
        # json.dumps avoids single-quote issues from str(dict)
        text_data = json.dumps(row.to_dict(), ensure_ascii=False)
        chunks = chunk_text(text_data)

        for chunk in chunks:
            vector = embedding_model.encode(chunk).tolist()
            rows_data.append({"content": chunk, "embedding": str(vector)})

        if progress_callback:
            progress_callback(i + 1, total)

    with engine.connect() as conn:
        conn.execute(text("DELETE FROM rag_data"))

        for item in rows_data:
            conn.execute(
                text("""
                    INSERT INTO rag_data (content, embedding)
                    VALUES (:content, CAST(:embedding AS vector))
                """),
                item
            )

        conn.commit()

    return len(rows_data)


def ask_question(question: str, chat_history: list[dict] = None) -> str:
    """
    Retrieve relevant context and generate an answer.
    chat_history: list of {"role": "user"/"assistant", "content": "..."} dicts.
    """
    query_vector = embedding_model.encode(question).tolist()

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT content
                FROM rag_data
                ORDER BY embedding <-> CAST(:vector AS vector)
                LIMIT 100
            """),
            {"vector": str(query_vector)}
        )
        rows = result.fetchall()

    if not rows:
        return "No data found in the knowledge base. Please upload and index a dataset first."

    context = "\n".join(row[0] for row in rows)

    system_prompt = """You are a data analyst assistant.
Answer only using the provided dataset context.
If the answer cannot be found in the context, say so clearly.
Always respond in this format:

**Summary:**
<one or two sentence overview>

**Key Findings:**
- <finding 1>
- <finding 2>
- ...

**Conclusion:**
<actionable takeaway or final note>"""

    messages = [{"role": "system", "content": system_prompt}]

    if chat_history:
        messages.extend(chat_history[-6:])  # keep last 3 exchanges for context

    messages.append({
        "role": "user",
        "content": f"Dataset context:\n{context}\n\nQuestion: {question}"
    })

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating response: {str(e)}"


def is_knowledge_base_ready() -> bool:
    """Check if there is any data in the RAG table."""
    try:
        init_db()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM rag_data"))
            count = result.scalar()
        return count > 0
    except Exception:
        return False