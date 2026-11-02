from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



def build_index(pdf_path):
    pages    = PyPDFLoader(pdf_path).load()                    # ① read all pages
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks   = splitter.split_documents(pages)                # ② chunk them
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db       = Chroma.from_documents(chunks, embedder)         # ③ in-memory store
    return db



model = ChatOpenAI(model="openai/gpt-oss-120b", temperature=0,api_key=os.getenv("GROQ_API_KEY"),
                            base_url=os.getenv("GROQ_BASE_URL"))

prompt = ChatPromptTemplate.from_template("""
You are a helpful PDF assistant. Answer the question using ONLY the context below.
If the context doesn't contain the answer, say "I couldn't find that in the document."
After your answer, list the page numbers you used as: Sources: page X, page Y.

Context:
{context}

Question: {question}
""")

def ask(db, question):
    chunks  = db.similarity_search(question, k=4)
    context = "\n\n".join(
        f"[page {c.metadata['page']+1}] {c.page_content}" for c in chunks)
    chain = prompt | model
    return chain.invoke({"context": context, "question": question}).content


# web view 

import gradio as gr

def upload(pdf, db_state):
    if pdf is None:
        return "❌ Upload failed.", db_state
    
    # Build index and update the state
    db_state = build_index(pdf.name)
    return "✅ PDF indexed! Ask me anything about it.", db_state
# The chat function now takes the db_state explicitly from the interface
def chat(message, history, db_state):
    if db_state is None:
        return "Please upload a PDF first 📄"
    return ask(db_state, message)

with gr.Blocks(title="📄 Chat with your PDF") as demo:
    gr.Markdown("## 📄 Chat with your PDF (powered by RAG)")
    
    # Define our state manager inside Blocks
    db_state = gr.State(None)
    
    pdf = gr.File(label="Upload a PDF", file_types=[".pdf"])
    status = gr.Markdown()
    
    # Pass db_state into the function, and let it update db_state output
    pdf.upload(upload, inputs=[pdf, db_state], outputs=[status, db_state])
    
    # Pass db_state as an additional input parameter to ChatInterface
    gr.ChatInterface(fn=chat, additional_inputs=[db_state])

demo.launch(share=True)