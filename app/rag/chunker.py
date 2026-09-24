"""
Utilities for splitting knowledge-base documents into chunks.
"""

import re

from app.rag.knowledge_loader import load_knowledge_base


def chunk_document(
    content: str,
) -> list[str]:
    """
    Split a Markdown document into section-based chunks.

    Each Markdown heading starts a new chunk.
    """

    sections = re.split(
        r"(?=^## )",
        content,
        flags=re.MULTILINE,
    )

    chunks = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        chunks.append(section)

    return chunks


def chunk_knowledge_base(
    knowledge_base_path: str,
) -> list[dict]:
    """
    Load the knowledge base and split each document into chunks.

    Each chunk keeps the original document metadata
    and its section heading.
    """

    documents = load_knowledge_base(knowledge_base_path)

    chunks = []

    for document in documents:
        document_chunks = chunk_document(
            document["content"]
        )

        for chunk in document_chunks:
            heading_match = re.match(
                r"^## (.+)",
                chunk,
            )

            if heading_match:
                section = heading_match.group(1).strip()
            else:
                section = "document"

            chunks.append(
                {
                    "file_name": document["file_name"],
                    "file_path": document["file_path"],
                    "content": chunk,
                    "section": section,
                }
            )

    return chunks