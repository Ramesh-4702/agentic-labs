# ⚡ agentic-labs

Welcome to **agentic-labs**, a comprehensive, modular laboratory showcasing modern Large Language Model (LLM) application design patterns. This repository bridges the gap between raw API orchestration and advanced agentic frameworks. 

It serves as a clean, copy-pasteable cookbook for developers looking to implement tools, conversational memory, Retrieval-Augmented Generation (RAG), and competitive LLM arenas.

---

## 🛠️ Tech Stack
*   **Core Orchestration:** LangChain, LangChain-OpenAI, LangChain-Groq
*   **Vector Database & Embeddings:** Chroma DB, HuggingFace (`all-MiniLM-L6-v2`)
*   **UI Playgrounds:** Gradio
*   **Web Scraping & Extraction:** BeautifulSoup4, Requests

---

## 🧪 What's Inside the Lab?

The repository features 5 primary architectural patterns:

### 1. 🤖 Tool-Calling Agents
*   **Function Execution:** Dynamically determines when to look up store pricing data or query live weather/population vectors.
*   **Self-Correction:** Built-in system instructions to automatically normalize user spelling mistakes (e.g., matching "sheos" to "shoes") before calling backend functions.

### 2. 📄 PDF Conversational RAG
*   **Document Pipelines:** In-memory vectorization using `PyPDFLoader` and `RecursiveCharacterTextSplitter`.
*   **Context Grounding:** Constrains the LLM to strictly cite and return precise page-number sources (`Sources: page X, page Y`).

### 3. 🧠 State & Conversational Memory
*   **Context Preservation:** Utilizes `MessagesPlaceholder` to dynamically feed a rolling loop of `HumanMessage` and `AIMessage` history back into the pipeline, preventing context loss.

### 4. ⚔️ LLM Arena (Model Battles)
*   **Side-by-Side Evaluation:** A unified Gradio front-end that accepts a single user prompt and maps it concurrently to competing back-end models (e.g., Qwen vs. GPT variants) with a real-time voting interface.

### 5. 🌐 Web Extraction Engine
*   **Content Sanitization:** A robust script utilizing BeautifulSoup4 to purge noise tags (`<script>`, `<style>`, `<nav>`, `<footer>`) and extract clean, structural textual layouts for downstream context injection.

---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com
cd agentic-labs
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file in the root directory:
```env
GROQ_API_KEY="your_groq_api_key_here"
GROQ_BASE_URL="https://groq.com"
```

### 3. Launch a Sandbox Playground
To spin up the RAG application:
```bash
python rag_app.py
```
