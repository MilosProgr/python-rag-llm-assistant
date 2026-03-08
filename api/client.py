import requests
import streamlit as st

def get_openai_response(input_text):
    url = "http://localhost:8000/essay/invoke"
    payload = {"input": {'topic': input_text}}
    response = requests.post(url, json=payload)
    return response.json()['output']['content']


def get_ollama_response(input_text):
    url = "http://localhost:8000/poem/invoke"
    payload = {"input": {'topic': input_text}}
    response = requests.post(url, json=payload)
    return response.json()['output']['content']

st.title("Chatbot with Langchain and Streamlit")

input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))