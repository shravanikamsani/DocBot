# 📚 DocBot: AI-Powered Document Assistant

DocBot is a high-speed, intelligent chatbot that allows users to upload PDF documents and get instant answers based on the content. It leverages frontier AI models and ultra-fast hardware to provide a seamless research experience.

## 🚀 Features
- **Ultra-Fast Inference:** Powered by **Groq LPU™** technology for near-instant responses.
- **Advanced Reasoning:** Uses the **Llama 3.3 70B** model to understand complex documents.
- **Beautiful UI:** A clean, responsive web interface built with **Streamlit**.
- **Secure Architecture:** Implements professional secret management for API safety.
- **RAG Implementation:** Uses a "Long-Context" approach to ensure high accuracy without hallucinations.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** Streamlit
- **LLM:** Meta Llama 3.3 70B (via Groq Cloud)
- **Document Processing:** PyPDF

---

## 📦 Project Structure
```text
docbot/
├── app.py              # Main application logic
├── requirements.txt    # Project dependencies
├── .streamlit/         # Local configuration (Do not upload to GitHub)
│   └── secrets.toml    # API Keys
└── README.md           # Project documentation