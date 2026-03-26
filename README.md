# Document QA Assistant

A question-answering assistant that ingests multi-source documents, structures them for retrieval, and answers questions using LangChain and an LLM backend.

---

## What It Does

- Loads documents from multiple sources (PDFs, text files, URLs)
- Splits and chunks documents using LangChain's text-splitting strategies
- Stores chunks in a vector store for semantic search
- Answers user questions by retrieving relevant context and passing it to an LLM

---

## Tech Stack

| Layer | Tool |
|---|---|
| Framework | LangChain |
| LLM | OpenAI (gpt-3.5-turbo) |
| Vector Store | FAISS |
| Embeddings | OpenAI Embeddings |
| Document Loaders | LangChain (PDF, TextFile, WebBase) |

---

## Project Structure

```
doc-qa-assistant/
├── data/                  # Raw input documents
├── src/
│   ├── loader.py          # Document loading logic
│   ├── splitter.py        # Text splitting strategies
│   ├── vectorstore.py     # Embedding + vector store setup
│   ├── retriever.py       # Retrieval logic
│   └── qa_chain.py        # QA chain assembly
├── main.py                # Entry point
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
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

---

## Usage

Place your documents in the `data/` folder, then run:

```bash
python main.py
```

You'll get an interactive prompt to ask questions against your documents.

---

## How It Works

```
Documents (PDF / TXT / URL)
        ↓
  Document Loaders
        ↓
  Text Splitter (chunks)
        ↓
  Embeddings → Vector Store
        ↓
  User Query → Retriever → Relevant Chunks
        ↓
  LLM → Answer
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key |

---

## Notes

- Default chunk size is 500 tokens with 50-token overlap
- FAISS index is built locally and not persisted between runs (can be enabled)
- Supports mixing document types in the `data/` folder
