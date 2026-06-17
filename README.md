# Agentic AI Learnings — AI Engineering Portfolio & Journey

Welcome! This repository documents my self-driven journey transitioning into an AI Engineer role. 

This repository contains hands-on implementations built from first principles. Rather than relying on automated LLM code generators or copy-pasting tutorials, I have focused on **learning from the ground up**—writing clean, production-grade Python code, implementing APIs, managing async concurrency, manipulating vectors with NumPy, and understanding the core mechanics of LLM tool calling, prompt engineering, and semantic search.

---

## 📅 Learning Roadmap & Progress

### Core AI Foundations
- [x] **Modern Python for AI** (Project: [Task Manager CLI](file:///Users/mano/workspace/agentic-ai-learnings/todo-app))
- [x] **APIs and Async Concurrency** (Project: [Multi-API Data Aggregator / Weather App](file:///Users/mano/workspace/agentic-ai-learnings/weather-app))
- [x] **LLM APIs & Chat Completions** (Project: [Terminal AI Assistant](file:///Users/mano/workspace/agentic-ai-learnings/terminal-chatbot))
- [x] **Prompt Engineering & Intent Detection** (Project: [Customer Support Classifier](file:///Users/mano/workspace/agentic-ai-learnings/support-ticket-classifier))
- [x] **Embeddings & Cosine Similarity** (Project: [Semantic Search Engine](file:///Users/mano/workspace/agentic-ai-learnings/semantic-search-engine))
- [ ] **Vector Databases & Metadata Filtering** (Project: Knowledge Base Search)
- [ ] **Independent Consolidation** (Rebuilding embeddings, search, classification, and assistant without templates)

### Production RAG (Upcoming)
- [ ] **Document Ingestion & Processing** (Project: PDF Ingestion Pipeline)
- [ ] **Basic RAG Architectures** (Project: PDF Question Answering)
- [ ] **Advanced Retrieval Layer** (Project: Smarter Retrieval Layer with query rewriting)
- [ ] **Hybrid Search Engines** (Project: Hybrid Search Engine combining BM25 and vector search)
- [ ] **Reranking Systems** (Project: Reranked RAG utilizing Cross Encoders)
- [ ] **RAG Evaluation Frameworks** (Project: RAG Test Suite validating faithfulness/groundedness)
- [ ] **Capstone Integration** (Project: Enterprise Knowledge Assistant with citations)

---

## 🛠️ Completed Projects

### 📂 Task Manager CLI ([todo-app](file:///Users/mano/workspace/agentic-ai-learnings/todo-app))
*A command-line task manager designed to practice clean Python structure and data validation.*
- **Features**: 
  - Complete CLI-based CRUD operations for managing tasks.
  - Local JSON-based persistence layer.
  - Strict input validation and serialization using Pydantic.
- **Tech Stack**: Python, Pydantic, JSON.

---

### 📂 Multi-API Data Aggregator ([weather-app](file:///Users/mano/workspace/agentic-ai-learnings/weather-app))
*An asynchronous app showcasing concurrent API communication, rate-limiting, and error-handling patterns.*
- **Features**:
  - Concurrent API calls to multiple weather and location data feeds.
  - Resilience strategies using asynchronous retries and exponential backoff.
  - Response caching to optimize performance and respect rate limits.
- **Tech Stack**: Python, `asyncio`, `httpx`, `tenacity`.

---

### 📂 Terminal AI Assistant ([terminal-chatbot](file:///Users/mano/workspace/agentic-ai-learnings/terminal-chatbot))
*An interactive CLI assistant interacting directly with LLMs.*
- **Features**:
  - Interactive terminal shell supporting streaming responses.
  - Structured JSON extraction from LLM completions.
  - Real-time token usage and cost tracking.
- **Tech Stack**: Python, OpenAI/Gemini SDKs, Pydantic.

---

### 📂 Customer Support Ticket Classifier ([support-ticket-classifier](file:///Users/mano/workspace/agentic-ai-learnings/support-ticket-classifier))
*A ticket categorization system demonstrating programmatic prompt engineering.*
- **Features**:
  - Multi-stage classification of inbound customer support tickets.
  - Sentiment analysis, intent detection, category routing, and priority scoring.
  - Outputs structured and validated directly using Pydantic schemas.
- **Tech Stack**: Python, OpenAI API, Pydantic.

---

### 📂 Semantic Search Engine ([semantic-search-engine](file:///Users/mano/workspace/agentic-ai-learnings/semantic-search-engine))
*A semantic search implementation showcasing vector representations and similarity metrics.*
- **Features**:
  - Document chunk loading and vector embedding generation using `sentence-transformers` (`all-MiniLM-L6-v2`).
  - Custom local JSON vector store storing float32 embeddings.
  - Cosine Similarity computation using PyTorch tensors.
  - Returns the top 5 most semantically relevant text chunks sorted by score.
- **Tech Stack**: Python, PyTorch, NumPy, `sentence-transformers`.

---

## ⚙️ Installation & Running the Projects

All projects share a common Python virtual environment setup at the root level.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/muralimano28/agentic-ai-learnings.git
   cd agentic-ai-learnings
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Run a Project**:
   Each subfolder contains its own dependencies and main script. To run any project (e.g., Semantic Search):
   ```bash
   cd semantic-search-engine
   pip install -r requirements.txt
   python -m app.main
   ```
