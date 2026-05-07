import streamlit as st
from groq import Groq
from pypdf import PdfReader
import os

# --- 1. CONFIGURATION ---
# Replace with your actual Groq API Key
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

# --- 2. UI DESIGN ---
st.set_page_config(page_title="DocuMind AI", page_icon="⚡", layout="centered")

# Custom CSS for a "Beautiful Web Page" look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    .stTextInput>div>div>input { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ DocBot: Groq Edition")
st.write("Upload a PDF and get instant answers powered by Llama 3.")

# Sidebar setup
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.header("Upload Zone")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    st.divider()
    st.info("Using Groq LPU™ for ultra-fast inference.")

# --- 3. HELPER FUNCTIONS ---
def get_pdf_text(file):
    text = ""
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

# --- 4. CHAT LOGIC ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if user_query := st.chat_input("Ask a question about your document..."):
    if not uploaded_file:
        st.error("Please upload a document first!")
    else:
        # Add user message to UI
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Generate Response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Extract text
                context = get_pdf_text(uploaded_file)
                
                # Call Groq API
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer questions accurately. If the answer is not in the text, say you don't know."},
                        {"role": "user", "content": f"Context: {context[:15000]}\n\nQuestion: {user_query}"}
                    ],
                    temperature=0.5,
                    max_tokens=1024,
                )
                
                response_text = completion.choices[0].message.content
                st.markdown(response_text)
                st.session_state.chat_history.append({"role": "assistant", "content": response_text})