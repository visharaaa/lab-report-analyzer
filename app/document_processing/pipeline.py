"""
High-level pipeline for processing laboratory report files.
"""

from pathlib import Path
from app.normalization.normalize_results import normalize_results

from app.document_processing.document_reader import (
    read_text_file,
    read_pdf_file,
    read_image_file,
    read_scanned_pdf_file,
)
from app.extraction.text_extractor import extract_results
from app.models.schemas import LabResult


def process_report(file_path: str | Path) -> list[LabResult]:
    """
    Read a laboratory report file and extract structured results.

    Supported formats:
    - TXT
    - PDF
    - PNG
    - JPG/JPEG
    """

    path = Path(file_path)

    suffix = path.suffix.lower()

    if suffix == ".txt":
        text = read_text_file(path)

    elif suffix == ".pdf":
        text = read_pdf_file(path)

        # If the PDF contains no extractable text,
        # treat it as a scanned PDF and use OCR.
        if not text.strip():
            text = read_scanned_pdf_file(path)

    elif suffix in {".png", ".jpg", ".jpeg"}:
        text = read_image_file(path)

    else:
        raise ValueError(
            f"Unsupported file format: {suffix}"
        )

    return extract_results(text)

    return normalize_results(results)