import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_documents(data_folder="data"):
    documents = []

    for filename in os.listdir(data_folder):
        filepath = os.path.join(data_folder, filename)

        if filename.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
            documents.extend(loader.load())

        elif filename.endswith(".txt"):
            loader = TextLoader(filepath)
            documents.extend(loader.load())

    print(f"Loaded {len(documents)} document chunks from {data_folder}/")
    return documents