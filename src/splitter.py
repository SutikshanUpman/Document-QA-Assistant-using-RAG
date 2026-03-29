from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    return chunks
```

---

**What each part does:**

- `chunk_size=500` — each chunk is max 500 characters
- `chunk_overlap=50` — chunks share 50 characters with the next one, so context isn't lost at the edges
- `RecursiveCharacterTextSplitter` — tries to split at paragraphs first, then sentences, then words. Smarter than just cutting at 500 chars blindly

---

**Visualising it:**
```
[ -------- chunk 1 -------- ]
                        [ -------- chunk 2 -------- ]
                                               [ -------- chunk 3 -------- ]
                        ↑ overlap              ↑ overlap