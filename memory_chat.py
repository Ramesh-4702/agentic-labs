from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-120b", temperature=0.3,api_key=os.getenv("GROQ_API_KEY"),
                            base_url="https://api.groq.com/openai/v1")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant. Use the conversation history to stay consistent."),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])
chain = prompt | model

"""# we hardcode the history here just to demonstrate
history = [HumanMessage("you are a LLM engineer"), AIMessage("yes i am llm engineer ,how can i help you ")]
"""

history = []                                   # ① starts EMPTY — nothing hardcoded

print("Chat with the bot (type 'quit' to exit).")
while True:                                     # ② one loop = one chat turn
    question = input("You: ")
    if question.strip().lower() in {"quit", "exit"}:
        break

    answer = chain.invoke(
        {"history": history, "question": question}).content   # ③ send history so far
    print("Bot:", answer)

    history.append(HumanMessage(question))      # ④ remember what you said...
    history.append(AIMessage(answer))           # ⑤ ...and what it replied
    print(f"   (history now has {len(history)} messages)")


answer = chain.invoke({"history": history, "question": "who are you what is your persona "})
print(answer.content)