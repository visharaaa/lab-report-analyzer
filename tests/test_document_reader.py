from pathlib import Path

import pytest

from app.document_processing.document_reader import (
    read_text_file,
    read_pdf_file,
    read_image_file,
    read_scanned_pdf_file,
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

def test_read_image_file(tmp_path):
    from PIL import Image, ImageDraw

    image_path = tmp_path / "sample_report.png"

    image = Image.new("RGB", (800, 200), "white")
    draw = ImageDraw.Draw(image)

    draw.text(
        (20, 20),
        "COMPLETE BLOOD COUNT\nHemoglobin 11.2 g/dL",
        fill="black",
    )

    image.save(image_path)

    text = read_image_file(image_path)

    assert "COMPLETE BLOOD COUNT" in text
    assert "Hemoglobin" in text
    assert "11.2" in text

def test_read_scanned_pdf_file(tmp_path):
    import pymupdf
    from PIL import Image, ImageDraw

    pdf_path = tmp_path / "scanned_report.pdf"
    image_path = tmp_path / "scanned_page.png"

    # Create an image containing laboratory report text.
    image = Image.new("RGB", (1200, 400), "white")
    draw = ImageDraw.Draw(image)

    draw.text(
        (50, 50),
        "COMPLETE BLOOD COUNT\nHemoglobin 11.2 g/dL",
        fill="black",
    )

    image.save(image_path)

    # Create a PDF containing the image as a scanned page.
    document = pymupdf.open()
    page = document.new_page(width=1200, height=400)

    page.insert_image(
        page.rect,
        filename=str(image_path),
    )

    document.save(pdf_path)
    document.close()

    # Read the scanned PDF using OCR.
    text = read_scanned_pdf_file(pdf_path)

    assert "COMPLETE BLOOD COUNT" in text
    assert "Hemoglobin" in text
    assert "11.2" in text