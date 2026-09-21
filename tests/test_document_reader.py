from pathlib import Path

import pytest

from app.document_processing.document_reader import (
    read_text_file,
    read_pdf_file,
)

def test_read_text_file():
    report_path = Path("data/sample_reports/sample_report.txt")

    text = read_text_file(report_path)

    assert "COMPLETE BLOOD COUNT" in text
    assert "Hemoglobin" in text
    assert "HbA1c" in text


def test_read_text_file_missing_file():
    missing_path = Path("data/sample_reports/does_not_exist.txt")

    with pytest.raises(FileNotFoundError):
        read_text_file(missing_path)


def test_read_pdf_file(tmp_path):
    import pymupdf

    pdf_path = tmp_path / "sample_report.pdf"

    document = pymupdf.open()
    page = document.new_page()

    page.insert_text(
        (72, 72),
        "COMPLETE BLOOD COUNT\nHemoglobin 11.2 g/dL"
    )

    document.save(pdf_path)
    document.close()

    text = read_pdf_file(pdf_path)

    assert "COMPLETE BLOOD COUNT" in text
    assert "Hemoglobin 11.2 g/dL" in text