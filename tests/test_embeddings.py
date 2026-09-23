from app.rag.embeddings import (
    generate_embeddings,
    load_embedding_model,
)

from app.rag.chunker import chunk_knowledge_base

def test_generate_embeddings():
    model = load_embedding_model()

    texts = [
        "Low hemoglobin may have several causes.",
        "Hemoglobin is a protein found in red blood cells.",
    ]

    embeddings = generate_embeddings(texts, model)

    assert embeddings.shape[0] == 2
    assert embeddings.shape[1] == 384

def test_generate_knowledge_base_embeddings():
    model = load_embedding_model()

    chunks = chunk_knowledge_base("knowledge_base")

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = generate_embeddings(
        texts,
        model,
    )

    assert embeddings.shape[0] == len(chunks)
    assert embeddings.shape[1] == 384