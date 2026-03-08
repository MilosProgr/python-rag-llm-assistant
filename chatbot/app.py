# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
#langsmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.Please respond to the user queries queries."),
        ("user", "Question: {topic}"),   
    ]
)

##streamlit framework
st.title("Chatbot with Langchain and Streamlit")
input_text = st.text_input("Enter your question here:")

#groq llm
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, max_tokens=150)
output_parser = StrOutputParser()
chain=prompt | llm | output_parser  

if input_text:
    st.write(chain.invoke({"question": input_text}))
