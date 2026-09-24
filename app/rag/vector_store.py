"""
Utilities for storing and searching knowledge-base embeddings
using ChromaDB.
"""

from pathlib import Path

import chromadb


COLLECTION_NAME = "medical_knowledge"


def create_vector_store(
    persist_directory: str | Path = "data/chroma",
):
    """
    Create or open a persistent ChromaDB collection.
    """

    client = chromadb.PersistentClient(
        path=str(persist_directory)
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection

def add_documents(
    collection,
    chunks: list[dict],
    embeddings,
) -> None:
    """
    Add knowledge-base chunks and their embeddings
    to a ChromaDB collection.
    """

    ids = [
        f"chunk_{index}"
        for index in range(len(chunks))
    ]

    documents = [
        chunk["content"]
        for chunk in chunks
    ]

    metadatas = [
    {
        "file_name": chunk["file_name"],
        "file_path": chunk["file_path"],
        "section": chunk.get("section", "unknown"),
    }
    for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas,
    )

def search_documents(
    collection,
    query_embedding,
    n_results: int = 3,
) -> list[dict]:
    """
    Search the vector store for the most relevant knowledge chunks.
    """

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return [
        {
            "content": document,
            "metadata": metadata,
            "distance": distance,
        }
        for document, metadata, distance
        in zip(documents, metadatas, distances)
    ]