# Personal AI Assistant using LangChain

A lightweight AI-powered personal chatbot built using LangChain, Streamlit, and Groq LLMs.

This project allows users to:

* Chat with an AI assistant
* Upload PDF/TXT documents
* Generate AI-powered summaries
* Ask questions based on uploaded documents

The application processes uploaded files temporarily in memory and does not permanently store user documents.

---

# Features

* Conversational AI chatbot
* PDF and TXT document upload
* AI-generated document summarization
* Question answering from uploaded files
* Real-time responses
* Lightweight and beginner-friendly implementation

---

# Technologies Used

* Python
* Streamlit
* LangChain
* Groq API
* Llama 3.1 Model
* PyPDF

---

# Project Architecture

```text
User Input / File Upload
            ↓
       Streamlit UI
            ↓
   LangChain Prompt Flow
            ↓
 Groq Llama 3.1 API Model
            ↓
 AI Generated Response
            ↓
      Display to User
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
cd YOUR_PROJECT_FOLDER
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Environment Variables

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_api_key_here
```

Get your free API key from:

https://console.groq.com

---

# Run The Application

```bash
streamlit run app.py
```

---

# Supported File Types

* PDF
* TXT

---

# Important Notes

* Uploaded files are processed temporarily during the active session only.
* No database or permanent storage is used.
* This project focuses on beginner-friendly AI workflow development using LangChain.

---

# Future Improvements

* DOCX support
* Multi-document chat
* Conversation memory
* Voice assistant integration
* RAG-based retrieval systems
* Cloud deployment

---

# License

This project is created for educational and learning purposes.
