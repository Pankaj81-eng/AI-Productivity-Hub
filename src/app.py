import streamlit as st
from summarizer import summarize_text
import docx
import PyPDF2

st.title("AI Productivity Hub - Document Summarizer")

uploaded_file = st.file_uploader("Upload a document (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])

content = ""
if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
    elif file_type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            content += page.extract_text()
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            content += para.text + "\n"

    st.write("File content:")
    st.write(content)
    if st.button("Summarize"):
        summary = summarize_text(content)
        st.subheader("Summary:")
        st.write(summary)