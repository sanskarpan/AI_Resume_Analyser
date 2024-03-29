import streamlit as st
# from dotenv import load_dotenv
from openai import OpenAI
import os

# # load_dotenv()
# openai.api_key = os.getenv('api_key')
OPENAI_API_KEY = st.secrets[OPENAI_API_KEY]
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'], 
)
st.title("Resume Feedback Application")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if uploaded_file is not None:
    try:
        resume_text = uploaded_file.read().decode('utf-8')
    except UnicodeDecodeError:
        resume_text = uploaded_file.read().decode('latin-1')

    client =  OpenAI()

    feedback = client.Completion.create(
        engine="gpt-3.5-turbo-instruct",  
        prompt=f"Provide feedback on this resume:\n{resume_text}\n---\n",
        temperature=0.5,
        max_tokens=400
    )
    
    st.subheader("Feedback on your resume:")
    st.write(feedback['choices'][0]['text'].strip())
