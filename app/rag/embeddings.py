"""
Utilities for generating embeddings for knowledge-base chunks.
"""

from sentence_transformers import SentenceTransformer
from functools import lru_cache

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def load_embedding_model() -> SentenceTransformer:
    """
    Load the pretrained embedding model.
    """

    return SentenceTransformer(MODEL_NAME)


def generate_embeddings(
    texts: list[str],
    model: SentenceTransformer,
):
    """
    Generate embeddings for a list of text chunks.
    """

    return model.encode(
        texts,
        convert_to_numpy=True,
    )