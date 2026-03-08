from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")



app = FastAPI(
    title="Chatbot API",
    description="API for a chatbot built with Langchain",
    version="1.0"
)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=150
)

prompt = ChatPromptTemplate.from_template(
    "Write an essay about {topic} in 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} in 100 words"
)

add_routes(app, prompt | model, path="/essay")
add_routes(app, prompt2 | model, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)