from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_vectorstore(chunks):
    print("Building vectorstore, this may take a moment...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    print("Vectorstore ready")
    return vectorstore
```

---

**What each part does:**

- `HuggingFaceEmbeddings` — loads a free local model that converts text to vectors
- `all-MiniLM-L6-v2` — a lightweight model, fast on CPU, good quality
- `FAISS.from_documents` — takes every chunk, embeds it, stores it in a searchable index

---

**Visualising it:**
```
"AI is a simulation..."  →  [0.23, 0.91, 0.04, ...]  ┐
"Deep learning uses..."  →  [0.11, 0.87, 0.33, ...]  ├─ FAISS Index
"NLP allows machines..." →  [0.67, 0.02, 0.88, ...]  ┘

Your question → vector → find closest vectors → return those chunks