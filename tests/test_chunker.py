from app.rag.chunker import (
    chunk_document,
    chunk_knowledge_base,
)


def test_chunk_document():
    content = """# Hemoglobin

## What it is

Hemoglobin is a protein in red blood cells.

## When the result is low

Low hemoglobin may have several causes.

## When the result is high

High hemoglobin may have several causes.
"""

    chunks = chunk_document(content)

    assert len(chunks) == 4
    assert chunks[0].startswith("# Hemoglobin")
    assert chunks[1].startswith("## What it is")
    assert "Low hemoglobin" in chunks[2]
    assert "High hemoglobin" in chunks[3]

def test_chunk_knowledge_base():
    chunks = chunk_knowledge_base("knowledge_base")

    assert len(chunks) > 18

    for chunk in chunks:
        assert "file_name" in chunk
        assert "file_path" in chunk
        assert "content" in chunk
        assert chunk["content"].strip() != ""

    file_names = {
        chunk["file_name"]
        for chunk in chunks
    }

    assert "hemoglobin.md" in file_names
    assert "fasting_blood_glucose.md" in file_names
    assert "hba1c.md" in file_names