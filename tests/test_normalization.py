from app.models.schemas import LabResult
from app.normalization.normalize_results import (
    normalize_result,
    normalize_results,
)


def test_normalize_result():
    result = LabResult(
        test_name="Haemoglobin",
        value=11.2,
        unit="g/dL",
    )

    normalized = normalize_result(result)

    assert normalized.test_name == "Haemoglobin"
    assert normalized.canonical_name == "hemoglobin"
    assert normalized.value == 11.2
    assert normalized.unit == "g/dL"


def test_normalize_unknown_test():
    result = LabResult(
        test_name="Unknown Test",
        value=10.0,
    )

    normalized = normalize_result(result)

    assert normalized.canonical_name is None


def test_normalize_results():
    results = [
        LabResult(
            test_name="Hb",
            value=11.2,
            unit="g/dL",
        ),
        LabResult(
            test_name="RBC Count",
            value=4.35,
            unit="10^12/L",
        ),
        LabResult(
            test_name="Fasting Blood Glucose",
            value=108.0,
            unit="mg/dL",
        ),
    ]

    normalized = normalize_results(results)

    assert len(normalized) == 3
    assert normalized[0].canonical_name == "hemoglobin"
    assert normalized[1].canonical_name == "rbc_count"
    assert normalized[2].canonical_name == "fasting_blood_glucose"