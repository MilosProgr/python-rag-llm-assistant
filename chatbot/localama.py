from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()   


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.Please respond to the user queries queries."),
        ("user", "Question: {question}"),   
    ]
)

st.title("Chatbot with Langchain and Streamlit")
input_text = st.text_input("Enter your question here:")

#groq llm
llm = Ollama(model="gemma", temperature=0.7)
output_parser = StrOutputParser()
chain=prompt | llm | output_parser  

if input_text:
    st.write(chain.invoke({"question": input_text}))

