# AI Paragraph Summarizer 📝

A simple and clean **Streamlit web app** that summarizes text or PDF documents using an LLM powered by **Groq (LLaMA 3.1)**.

---

## 🚀 Features

- ✍️ Paste text or upload **TXT / PDF**
- 📏 Choose summary length (word limit)
- ⚡ Fast summarization using Groq API
- 📄 Clean, compact UI
- ⬇️ Download summary as a text file

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Groq API (LLaMA 3.1)**
- **PyPDF2**
- **python-dotenv**

---

## 📂 Project Structure

.
├── app.py
├── requirements.txt
├── README.md
└── .env (not pushed to GitHub)

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
