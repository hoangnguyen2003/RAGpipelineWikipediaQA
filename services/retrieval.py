import faiss
import numpy as np

def build_faiss_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index

def retrieve_chunks(query, index, embedding_model, chunks, k=3):
    query_embedding = embedding_model.encode([query])
    _, indices = index.search(np.array(query_embedding), k)
    return [chunks[i] for i in indices[0]]