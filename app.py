
import streamlit as st
from io import StringIO
import pymupdf
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

st.title("LLM")
user_question=st.text_input("Enter Question").strip()
uploaded_file = st.file_uploader("Choose a file")

response=None
if uploaded_file is not None:
    doc = pymupdf.open(stream=uploaded_file.read(), filetype="pdf")
    file=""
    for page in doc:
        file=file+page.get_text()
    st.write(file)
    client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response=client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=user_question+file,
)
if response:
    st.write(response.text)