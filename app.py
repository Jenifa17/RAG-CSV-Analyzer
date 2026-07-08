import streamlit as st
import pandas as pd
from rag import store_data, ask_question, is_knowledge_base_ready

st.set_page_config(
    page_title="AI Data Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Dataset RAG Assistant")
st.caption("Upload a CSV, build a knowledge base, then ask questions about your data.")

# ── Session state ──────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []   # list of {"role": ..., "content": ...}

if "kb_ready" not in st.session_state:
    st.session_state.kb_ready = is_knowledge_base_ready()

# ── Sidebar: upload & index ────────────────────────────────────────────────────
with st.sidebar:
    st.header("📂 Dataset")
    file = st.file_uploader("Upload CSV", type="csv")

    if file:
        try:
            df = pd.read_csv(file)
            st.success(f"Loaded {len(df):,} rows × {len(df.columns)} columns")
            st.dataframe(df, use_container_width=True)

            if st.button("⚡ Build Knowledge Base", use_container_width=True):
                progress_bar = st.progress(0, text="Embedding rows…")

                def update_progress(current, total):
                    pct = int(current / total * 100)
                    progress_bar.progress(pct, text=f"Embedding row {current}/{total}…")

                with st.spinner("Storing embeddings…"):
                    chunks_stored = store_data(df, progress_callback=update_progress)

                progress_bar.empty()
                st.success(f"Knowledge base ready — {chunks_stored} chunks indexed.")
                st.session_state.kb_ready = True
                st.session_state.chat_history = []  # reset chat on new dataset

        except Exception as e:
            st.error(f"Failed to load file: {e}")

    st.divider()

    if st.session_state.kb_ready:
        st.success("✅ Knowledge base is ready")
    else:
        st.warning("⚠️ No knowledge base yet. Upload a CSV and click Build.")

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# ── Main: chat interface ───────────────────────────────────────────────────────
chat_container = st.container()

with chat_container:
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

question = st.chat_input(
    "Ask a question about your dataset…",
    disabled=not st.session_state.kb_ready
)

if not st.session_state.kb_ready and not question:
    st.info("Upload a CSV file and build the knowledge base to start chatting.")

if question:
    if not st.session_state.kb_ready:
        st.warning("Please build the knowledge base first.")
    else:
        # Show user message immediately
        st.session_state.chat_history.append({"role": "user", "content": question})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(question)

        # Generate and show assistant response
        with chat_container:
            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    answer = ask_question(
                        question,
                        chat_history=st.session_state.chat_history[:-1]
                    )
                st.markdown(answer)

        st.session_state.chat_history.append({"role": "assistant", "content": answer})