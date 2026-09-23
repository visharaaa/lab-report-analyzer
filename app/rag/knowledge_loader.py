"""
Utilities for loading medical knowledge-base documents.
"""

from pathlib import Path


def load_knowledge_base(
    knowledge_base_path: str | Path,
) -> list[dict]:
    """
    Load all Markdown documents from the knowledge base.

    Returns a list of dictionaries containing:
    - file name
    - file path
    - document content
    """

    path = Path(knowledge_base_path)

    documents = []

    for file_path in sorted(path.rglob("*.md")):
        content = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "file_name": file_path.name,
                "file_path": str(file_path),
                "content": content,
            }
        )

    return documents