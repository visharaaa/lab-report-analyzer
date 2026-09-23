import numpy as np

from app.rag.vector_store import (
    add_documents,
    create_vector_store,
)

def test_create_vector_store(tmp_path):
    collection = create_vector_store(
        tmp_path / "chroma"
    )

    assert collection.name == "medical_knowledge"
    assert collection.count() == 0

def test_add_documents(tmp_path):
    collection = create_vector_store(
        tmp_path / "chroma"
    )

    chunks = [
        {
            "file_name": "hemoglobin.md",
            "file_path": "knowledge_base/cbc/hemoglobin.md",
            "content": "Low hemoglobin may have several causes.",
        },
        {
            "file_name": "hba1c.md",
            "file_path": "knowledge_base/hba1c/hba1c.md",
            "content": "HbA1c reflects average blood glucose over time.",
        },
    ]

    embeddings = np.array(
        [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
        ]
    )

    add_documents(
        collection,
        chunks,
        embeddings,
    )

    assert collection.count() == 2

