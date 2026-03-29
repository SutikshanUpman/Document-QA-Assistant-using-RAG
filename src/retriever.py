def get_retriever(vectorstore):
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )
    return retriever
```

---

**What each part does:**

- `as_retriever()` — wraps the FAISS index into a retriever LangChain can use
- `k=3` — return the 3 most relevant chunks for any question

---

**Visualising the full flow so far:**
```
data/sample.txt
      ↓ loader.py
  [full document]
      ↓ splitter.py
  [chunk1, chunk2, chunk3 ...]
      ↓ vectorstore.py
  [FAISS Index with vectors]
      ↓ retriever.py
  "What is deep learning?" → top 3 matching chunks