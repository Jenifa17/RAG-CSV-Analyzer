# 🤖 RAG CSV Analyzer

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to interact with any CSV files using natural language queries. The application converts user questions into SQL queries, retrieves relevant information from a PostgreSQL database, and generates accurate AI-powered responses.

---

## 🚀 Features

- 📂 Upload and analyze CSV datasets
- 🗄️ Store data in PostgreSQL
- 🤖 Ask questions in natural language
- 🔍 AI converts questions into SQL queries
- 📊 Retrieve relevant information from the database
- 💬 Generate structured AI-powered responses
- 🌐 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PostgreSQL
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
git clone https://github.com/Jenifa17/RAG-CSV-Analyzer.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the environment file

Copy:

```
.env.example
```

to

```
.env
```

and add your credentials:

```env
OPENROUTER_API_KEY=your_api_key
DATABASE_URL=your_database_url
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Query

**Question:**

> Who are high-risk patients for heart disease?

**Output:**

The application retrieves relevant patient records from PostgreSQL and generates structured AI insights using the OpenRouter LLM.

---

## 📸 Application Screenshots

### 1️⃣ CSV Upload

![CSV Upload](images/upload_page.png)

### 2️⃣ Dataset Preview

![Dataset Preview](images/dataset_preview.png)

### 3️⃣ AI Generated Response

![AI Response](images/ai_response.png)

---

## 📁 Project Structure

```
health_checkup-RAG-Project/
│── app.py
│── database.py
│── rag.py
│── requirements.txt
│── README.md
│── .env.example
│── images/
│    ├── upload_page.png
│    ├── dataset_preview.png
│    └── ai_response.png
```

---

## 🔄 Project Workflow

```
CSV Dataset
      │
      ▼
PostgreSQL Database
      │
      ▼
Natural Language Question
      │
      ▼
RAG Engine
      │
      ▼
OpenRouter LLM
      │
      ▼
Generated SQL Query
      │
      ▼
Retrieve Relevant Data
      │
      ▼
AI Generated Answer
```

---

## 🎯 Future Enhancements

- Support multiple datasets
- Data visualization dashboards
- Chat history
- User authentication
- Export AI-generated reports
- Cloud deployment

---

## 👩‍💻 Author

**Jenifa**

Electronics and Communication Engineering (ECE)

Python Developer | AI & Data Enthusiast
