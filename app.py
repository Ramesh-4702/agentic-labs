
import gradio as gr
from agent import agent          


def chat(message, history):

    return agent(message)


gr.ChatInterface(
    fn=chat,
    title="🛍️ Smart Shop Assistant",
    description="Ask me the price of shoes, hat, bag, shorts or pants — I'll look it up.",
).launch(share=True)  
