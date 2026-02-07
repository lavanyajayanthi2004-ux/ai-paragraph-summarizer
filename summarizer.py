import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader

# ======================
# ENV
# ======================
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="AI Paragraph Summarizer",
    layout="wide"
)

# ======================
# COMPACT CSS
# ======================
st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 1rem;
}
h1, h2, h3 {
    margin-bottom: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER (COMPACT)
# ======================
st.markdown("## AI Paragraph Summarizer")
st.caption("Summarize text or documents using simple language")
st.divider()

# ======================
# LAYOUT
# ======================
left_col, right_col = st.columns([1.1, 1])

# ======================
# LEFT → INPUT
# ======================
with left_col:
    st.markdown("### Input")

    word_limit = st.number_input(
        "Summary length (words)",
        min_value=50,
        max_value=500,
        value=200,
        step=10
    )

    uploaded_file = st.file_uploader(
        "Upload TXT or PDF (optional)",
        type=["txt", "pdf"]
    )

    text = ""
    if uploaded_file:
        if uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode("utf-8")
        else:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    text = st.text_area(
        "Text to summarize",
        value=text,
        height=200,
        placeholder="Paste text here or upload a file..."
    )

    summarize = st.button("Summarize", use_container_width=True)

# ======================
# RIGHT → SUMMARY
# ======================
with right_col:
    st.markdown("### Summary")
    output = st.empty()

    if summarize:
        if not text.strip():
            st.warning("Please enter text or upload a file.")
        else:
            with st.spinner("Summarizing..."):
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "system",
                            "content": f"Summarize the text in about {word_limit} words using simple language."
                        },
                        {
                            "role": "user",
                            "content": text
                        }
                    ],
                    temperature=0.5
                )

                summary = response.choices[0].message.content

                output.markdown(
                    f"""
                    <div style="
                        padding: 0.8rem;`
                        border-radius: 8px;
                        background-color: rgba(127,127,127,0.1);
                        line-height: 1.55;
                        font-size: 0.9rem;
                    ">
                    {summary}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.download_button(
                    "Copy Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain",
                    use_container_width=True
                )
