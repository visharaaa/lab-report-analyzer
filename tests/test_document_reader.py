from pathlib import Path

import pytest

from app.document_processing.document_reader import read_text_file


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