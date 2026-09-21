from pathlib import Path

from app.document_processing.pipeline import process_report


def test_process_text_report():
    report_path = Path("data/sample_reports/sample_report.txt")

    results = process_report(report_path)

    assert len(results) == 16

    results_by_name = {
        result.canonical_name: result
        for result in results
    }

    assert results_by_name["hemoglobin"].value == 11.2
    assert results_by_name["hemoglobin"].flag == "low"

    assert results_by_name["hemoglobin"].test_name == "Hemoglobin"
    assert results_by_name["hemoglobin"].canonical_name == "hemoglobin"

    assert results_by_name["fasting_blood_glucose"].value == 108.0
    assert results_by_name["fasting_blood_glucose"].flag == "high"

    assert results_by_name["hba1c"].value == 5.9
    assert results_by_name["hba1c"].flag == "high"