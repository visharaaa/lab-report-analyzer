"""
Build the searchable vector index from the medical knowledge base.
"""

from app.rag.chunker import chunk_knowledge_base
from app.rag.embeddings import (
    generate_embeddings,
    load_embedding_model,
)
from app.rag.vector_store import (
    add_documents,
    create_vector_store,
)


def index_knowledge_base(
    knowledge_base_path: str = "knowledge_base",
    persist_directory: str = "data/chroma",
) -> int:
    """
    Load, chunk, embed, and store the knowledge base.

    Returns the number of indexed chunks.
    """

    chunks = chunk_knowledge_base(
        knowledge_base_path
    )

    model = load_embedding_model()

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = generate_embeddings(
        texts,
        model,
    )

    collection = create_vector_store(
        persist_directory
    )

    add_documents(
        collection,
        chunks,
        embeddings,
    )

    return collection.count()