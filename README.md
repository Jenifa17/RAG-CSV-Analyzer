# 🤖  RAG CSV Analyzer

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to interact with any CSV dataset using natural language queries. The application converts CSV data into vector embeddings, stores them in PostgreSQL with pgvector, and generates accurate AI-powered responses using semantic search.

---

## 🚀 Features

- 📂 Upload and analyze any CSV dataset
- 🧠 Convert text data into vector embeddings
- 🗄️ Store embeddings in PostgreSQL + pgvector
- 🔍 Semantic similarity search on your data
- 🤖 Ask questions in natural language
- 💬 Get structured AI-powered responses
- 🌐 Interactive Streamlit web interface
- 💬 Chat history support

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PostgreSQL + pgvector
- Sentence Transformers (all-MiniLM-L6-v2)
- SQLAlchemy
- Pandas
- OpenRouter LLM API
- python-dotenv

---

## 📊 Dataset

- **Dataset:** Health Checkup Dataset
- **Rows:** 99
- **Columns:** 19

---

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jenifa17/health_checkup-RAG-Project.git
```

### 2. Install dependencies

```bash
pip install streamlit sqlalchemy psycopg2-binary sentence-transformers openai python-dotenv pandas
```

### 3. Create the environment file

Copy `.env.example` to `.env` and add your credentials:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
API_KEY=your_openrouter_api_key
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Query

**Question:**
> which age group has highest BMI

**Output:**
## 📸 Screenshots

### 1️⃣ CSV Upload
![CSV Upload](Screenshot%202026-07-09%20213226.png)

### 2️⃣ Dataset Preview  
![Dataset Preview](Screenshot%202026-07-09%20213449.png)

### 3️⃣ AI Response
![AI Response](Screenshot%202026-07-08%20213229.png)

**Summary:**
The highest BMI in the dataset is **46.11**, belonging to an individual in the **60–64** age group.

**Key Findings:**
- Maximum BMI: **46.11** (Obese Class III)
- Age group: **60–64**
- Next highest BMIs: **45.33** and **43.94**

**Conclusion:**
The **60–64** age group contains the individual with the highest BMI in the dataset.

---

## 📁 Project Structure

```
health_checkup-RAG-Project/
│── app.py
│── database.py
│── rag.py
│── .env example
│── README.md
```

---

## 🔄 How RAG Works

```
CSV Dataset
      │
      ▼
Text Conversion (each row → string)
      │
      ▼
Vector Embeddings (Sentence Transformers)
      │
      ▼
Store in PostgreSQL + pgvector
      │
      ▼
User asks a Natural Language Question
      │
      ▼
Question → Vector Embedding
      │
      ▼
Semantic Similarity Search (pgvector)
      │
      ▼
Top 5 Relevant Rows retrieved as Context
      │
      ▼
LLM (via OpenRouter API)
      │
      ▼
Structured AI Answer ✅
```

---

## 🎯 Future Enhancements

- Support multiple datasets simultaneously
- Data visualization dashboards
- User authentication
- Export AI-generated reports
- Cloud deployment (Streamlit Cloud)

---

## 👩‍💻 Author

**Jenifa**

Electronics and Communication Engineering (ECE)

Python Developer | AI & ML Enthusiast
