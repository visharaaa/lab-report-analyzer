"""
Utilities for reading laboratory report documents.
"""

from pathlib import Path


def read_text_file(file_path: str | Path) -> str:
    """
    Read a text-based laboratory report and return its contents.
    """

    path = Path(file_path)

    return path.read_text(encoding="utf-8")