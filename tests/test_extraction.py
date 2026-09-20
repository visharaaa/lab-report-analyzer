from pathlib import Path

from app.extraction.text_extractor import extract_results


def test_sample_report_extraction():
    report_path = Path("data/sample_reports/sample_report.txt")

    text = report_path.read_text()

    results = extract_results(text)

    # We expect all 16 supported results from the sample report.
    assert len(results) == 16

    results_by_name = {
        result.canonical_name: result
        for result in results
    }

    # Hemoglobin
    hemoglobin = results_by_name["hemoglobin"]

    assert hemoglobin.value == 11.2
    assert hemoglobin.unit == "g/dL"
    assert hemoglobin.reference_low == 12.0
    assert hemoglobin.reference_high == 15.0
    assert hemoglobin.flag == "low"

    # RBC
    rbc = results_by_name["rbc_count"]

    assert rbc.value == 4.35
    assert rbc.unit == "10^12/L"
    assert rbc.flag == "normal"

    # WBC
    wbc = results_by_name["wbc_count"]

    assert wbc.value == 7.4
    assert wbc.unit == "10^9/L"
    assert wbc.flag == "normal"

    # Platelets
    platelets = results_by_name["platelet_count"]

    assert platelets.value == 280.0
    assert platelets.unit == "10^9/L"
    assert platelets.flag == "normal"

    # Fasting blood glucose
    glucose = results_by_name["fasting_blood_glucose"]

    assert glucose.value == 108.0
    assert glucose.unit == "mg/dL"
    assert glucose.flag == "high"

    # HbA1c
    hba1c = results_by_name["hba1c"]

    assert hba1c.value == 5.9
    assert hba1c.unit == "%"
    assert hba1c.flag == "high"