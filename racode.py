import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI 
import os
load_dotenv()


client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


st.title("Resume Feedback Application")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if uploaded_file is not None:
    try:
        resume_text = uploaded_file.read().decode('utf-8')
    except UnicodeDecodeError:
        resume_text = uploaded_file.read().decode('latin-1')

    try:
        feedback = client.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
            messages=[{"role": "user", "content":"Provide feedback on this resume:\n{resume_text}"}],
            stream =True,          
        )
    except ZeroDivisionError:
        st.error(f"OpenAI API error")  
    else:
        st.subheader("Feedback on your resume:")
        st.write(feedback.choices[0].text)
