import streamlit as st
import openai

openai.api_key = "EnterYourAPIKey" 
st.title("Resume Feedback Application")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if uploaded_file is not None:
    try:
        resume_text = uploaded_file.read().decode('utf-8')
    except UnicodeDecodeError:
        resume_text = uploaded_file.read().decode('latin-1')

    try:
        feedback = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  
            prompt=f"Provide feedback on this resume:\n{resume_text}\n---\n",
            temperature=0.5,
            max_tokens=400
        )
    except openai.error.InvalidRequestError as e:
        st.error(f"OpenAI API error: {str(e)}")  
    else:
        st.subheader("Feedback on your resume:")
        st.write(feedback['choices'][0]['text'].strip())
