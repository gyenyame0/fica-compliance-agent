from utils.prompts import str_drafting_prompt
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_str(summary):
    prompt = str_drafting_prompt(summary)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
