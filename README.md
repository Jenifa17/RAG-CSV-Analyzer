# 🤖  RAG Data Assistant

An AI-powered Data Assistant that lets you 
chat with your own CSV dataset using 
natural language!

## 🛠️ Tech Stack
- Python + Streamlit
- PostgreSQL + pgvector
- Sentence Transformers (all-MiniLM-L6-v2)
- OpenRouter LLM API

## ⚡ How to Run

1. Clone this repo
2. Install dependencies:
pip install streamlit sqlalchemy psycopg2-binary
sentence-transformers openai python-dotenv pandas

3. Copy .env.example → .env and fill your credentials
4. Run:
streamlit run app.py

## 📊 Features
- Upload any CSV dataset
- Build vector knowledge base  
- Ask questions in natural language
- Get structured AI answers

## 🧪 Tested With
- Health Checkup Dataset (99 rows × 19 columns)
- Asked: "Who are high risk patients for heart disease?"
- Got structured insights instantly!
