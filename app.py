
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("My First Agentic AI")

question = st.text_input("Ask a question")

if st.button("Submit"):

    if question:

        response = model.generate_content(question)

        st.write(response.text)
