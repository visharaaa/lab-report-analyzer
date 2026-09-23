"""
Utilities for retrieving relevant medical knowledge.
"""

from app.rag.embeddings import (
    generate_embeddings,
    load_embedding_model,
)
from app.rag.vector_store import (
    create_vector_store,
    search_documents,
)


def retrieve_knowledge(
    query: str,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> list[dict]:
    """
    Retrieve the most relevant knowledge chunks for a query.
    """

    model = load_embedding_model()

    query_embedding = generate_embeddings(
        [query],
        model,
    )[0]

    collection = create_vector_store(
        persist_directory
    )

    return search_documents(
        collection,
        query_embedding,
        n_results=n_results,
    )