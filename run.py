from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents

documents = load_file(Path("data/sample_kb/company_it_handbook.md"))
print(f"Documents loaded: {len(documents)}")
print(f"Documents: {documents}")
print("================================")
chunks = chunk_documents(documents)
print(f"Documents chunked: {len(chunks)}")
print(f"Chunked Documents: {chunks}")
print("================================")
add_documents(chunks)


