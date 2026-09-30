import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATA_DIR = "data"
DB_DIR = "./vector_db"

print("1. Loading HuggingFace Embedding Model (all-MiniLM-L6-v2)...")
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embedding_model
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=100
)

files_to_process = []
for root, _, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith((".pdf", ".txt", ".docx")):
            files_to_process.append(os.path.join(root, file))

print(f"2. Found {len(files_to_process)} files in data/ folder.")

total_chunks = 0
for idx, file_path in enumerate(files_to_process, start=1):
    print(f"[{idx}/{len(files_to_process)}] Processing: {file_path}...")
    try:
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        else:
            loader = TextLoader(file_path, encoding="utf-8")

        docs = loader.load()
        chunks = text_splitter.split_documents(docs)

        for chunk in chunks:
            chunk.metadata["source_file"] = os.path.basename(file_path)

        if chunks:
            vector_store.add_documents(chunks)
            total_chunks += len(chunks)
            print(f"   -> Added {len(chunks)} chunks.")
    except Exception as e:
        print(f"   ⚠️ Skipped {file_path}: {e}")

print(f"\n✅ SUCCESS! Total {total_chunks} chunks embedded into {DB_DIR}")

# Quick verification test
print("\n--- Testing Vector Search ---")
test_results = vector_store.similarity_search("What are the units in Object Oriented Programming?", k=2)
for i, res in enumerate(test_results, 1):
    print(f"\nMatch {i} (Source: {res.metadata.get('source_file')}):")
    print(res.page_content[:250] + "...")