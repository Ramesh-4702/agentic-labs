# config.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from the .env file
load_dotenv()

# Initialize the reusable client
client = ChatOpenAI(
    model="openai/gpt-oss-120b", 
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY"), 
    base_url=os.getenv("GROQ_BASE_URL")
)
