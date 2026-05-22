# 📘 AI Research Assistant

An AI-powered PDF Question Answering application built using Streamlit, LangChain, FAISS, HuggingFace Embeddings, and Google Gemini API.

Upload any PDF document and ask questions directly from it. The application retrieves relevant information from the uploaded document and generates intelligent answers using Retrieval-Augmented Generation (RAG).

---

## 🌐 Live Demo

Try the deployed application:

https://ai-research-assistant-lqw8knbqqdr8hcq6hmcddv.streamlit.app/

---

## 📂 GitHub Repository

Source code:

https://github.com/SadiyaBanu196/ai-research-assistant

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract text from uploaded PDFs
- ✂️ Automatic text chunking
- 🧠 Vector search using FAISS
- 🤖 AI-powered PDF Question Answering
- 💬 Interactive chatbot interface
- 📚 Retrieval-Augmented Generation (RAG)
- ⚡ Supports different PDF document types
- 🌐 Cloud deployment using Streamlit

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI / Machine Learning
- LangChain
- FAISS Vector Store
- Google Gemini API
- HuggingFace Embeddings

### PDF Processing
- PyPDF

---

## 📂 Project Structure

```text
ai-research-assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── chatbot.py
│   ├── pdf_handler.py
│   └── vector_store.py
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SadiyaBanu196/ai-research-assistant.git
```

Move into project directory:

```bash
cd ai-research-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create Streamlit secrets file:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GOOGLE_API_KEY="YOUR_API_KEY"
```

Run the application:

```bash
streamlit run app.py
```

---

## 🧩 How It Works

1. Upload PDF document
2. Extract text from PDF
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in FAISS vector database
6. User asks a question
7. Retrieve relevant context
8. Gemini API generates response from retrieved information

---

## 📈 Future Improvements

- Multi-PDF support
- Source citations
- Confidence score display
- Better retrieval optimization
- Improved UI/UX
- Chat export functionality

---

## 🎯 Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- LangChain workflows
- FAISS integration
- LLM API integration
- Streamlit deployment
- End-to-end AI application development

---

## 👨‍💻 Author

Sadiya Banu Syed

Engineering Student | AI & Machine Learning Enthusiast
