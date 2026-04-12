# Document QA Assistant
### Generative AI Application | RAG + LangChain + FAISS + OpenAI

A production-style question-answering system built as part of the **IBM Generative AI Engineering** curriculum on Coursera. Demonstrates end-to-end retrieval-augmented generation (RAG) — from multi-source document ingestion to LLM-powered answers via a conversational interface.

---

## Objective

Build a real-world AI application that can **ingest documents from multiple sources, semantically retrieve relevant context, and answer natural language questions** — without hallucinating or relying solely on the LLM's training data.

This project bridges the gap between raw document storage and intelligent, context-aware Q&A by combining vector search with large language models through a structured RAG pipeline.

---

## Core Stages

### 1. Document Ingestion
Load content from heterogeneous sources using LangChain's document loaders — PDFs, plain text files, and web URLs — into a unified document format ready for downstream processing.

### 2. Text Splitting
Apply chunking strategies (fixed-size with overlap) to break large documents into semantically coherent segments. Chunk size and overlap are tuned to balance retrieval precision with context completeness.

### 3. Embedding + Vector Store
Generate dense vector embeddings for each chunk using OpenAI Embeddings and index them in a **FAISS** vector store for fast approximate nearest-neighbor search at query time.

### 4. Retrieval
On each user query, the retriever performs semantic similarity search over the FAISS index to surface the most relevant document chunks — replacing keyword matching with meaning-based retrieval.

### 5. LLM-Powered Answer Generation
Retrieved chunks are injected into a prompt and passed to **GPT-3.5-turbo** via a LangChain QA chain. The model synthesizes a grounded answer using only the retrieved context, reducing hallucination.

---

## Final Output

- **Interactive CLI Q&A interface** — ask questions in plain English, get answers grounded in your documents
- **Modular RAG pipeline** — each stage (loading, splitting, embedding, retrieval, generation) is independently testable and swappable
- **Portfolio-ready codebase** — structured for readability, extensibility, and real-world deployment

---

## Tech Stack

| Layer | Tool |
|---|---|
| Framework | LangChain |
| LLM | OpenAI GPT-3.5-turbo |
| Vector Store | FAISS |
| Embeddings | OpenAI Embeddings |
| Document Loaders | LangChain (PDF, TextFile, WebBase) |
| Interface | Python CLI |

---

## Project Structure

```
doc-qa-assistant/
├── data/                  # Raw input documents (PDF, TXT, URLs)
├── src/
│   ├── loader.py          # Multi-source document loading
│   ├── splitter.py        # Chunking strategies with overlap
│   ├── vectorstore.py     # Embedding generation + FAISS indexing
│   ├── retriever.py       # Semantic similarity retrieval
│   └── qa_chain.py        # LangChain QA chain assembly
├── main.py                # Entry point + interactive prompt loop
├── .env                   # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## Setup

```bash
git clone <repo-url>
cd doc-qa-assistant
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_key_here
```

Place documents in the `data/` folder, then run:
```bash
python main.py
```

---

## Pipeline Architecture

```
Documents (PDF / TXT / URL)
        ↓
  Document Loaders          ← LangChain WebBase, PyPDF, TextFile
        ↓
  Text Splitter             ← 500-token chunks, 50-token overlap
        ↓
  OpenAI Embeddings         ← dense vector representations
        ↓
  FAISS Vector Store        ← local index, similarity search
        ↓
  User Query → Retriever    ← top-k semantically relevant chunks
        ↓
  GPT-3.5-turbo → Answer    ← context-grounded response
```

---

## Configuration

| Parameter | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | — | OpenAI API key (required) |
| Chunk size | 500 tokens | Size of each document segment |
| Chunk overlap | 50 tokens | Overlap between adjacent chunks |
| FAISS persistence | Disabled | Enable to reuse index across runs |

---

*Built as part of the IBM Generative AI Engineering Professional Certificate — [Project: Generative AI Applications with RAG and LangChain](https://www.coursera.org/learn/project-generative-ai-applications-with-rag-and-langchain) on Coursera.*
