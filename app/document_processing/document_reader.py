"""
Utilities for reading laboratory report documents.
"""

from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def read_text_file(file_path: str | Path) -> str:
    """
    Read a text-based laboratory report and return its contents.
    """

    path = Path(file_path)

    return path.read_text(encoding="utf-8")

def read_pdf_file(file_path: str | Path) -> str:
    """
    Extract text from a text-based PDF laboratory report.
    """

    path = Path(file_path)

    text = ""

    with pymupdf.open(path) as document:
        for page in document:
            text += page.get_text()

    return text

def read_image_file(file_path: str | Path) -> str:
    """
    Extract text from an image-based laboratory report using OCR.
    """

    path = Path(file_path)

    image = Image.open(path)

    return pytesseract.image_to_string(image)
