from app.models.schemas import LabResult
from app.rag.context_builder import (
    build_report_context,
    build_result_context,
)


def test_build_result_context():
    result = LabResult(
        test_name="Hemoglobin",
        canonical_name="hemoglobin",
        value=11.2,
        unit="g/dL",
        reference_low=12.0,
        reference_high=15.0,
        flag="low",
    )

    retrieved_chunks = [
        {
            "content": "A low hemoglobin result may have several possible causes.",
            "metadata": {
                "file_name": "hemoglobin.md",
            },
            "distance": 0.4,
        }
    ]

    context = build_result_context(
        result,
        retrieved_chunks,
    )

    assert "Test: hemoglobin" in context
    assert "Result: 11.2 g/dL" in context
    assert "Status: low" in context
    assert "hemoglobin.md" in context
    assert "A low hemoglobin result" in context


def test_build_report_context():
    results = [
        LabResult(
            test_name="Hemoglobin",
            canonical_name="hemoglobin",
            value=11.2,
            unit="g/dL",
            reference_low=12.0,
            reference_high=15.0,
            flag="low",
        ),
        LabResult(
            test_name="WBC",
            canonical_name="wbc_count",
            value=7.4,
            unit="10^9/L",
            reference_low=4.0,
            reference_high=11.0,
            flag="normal",
        ),
    ]

    retrieved_knowledge = {
        "hemoglobin": [
            {
                "content": "A low hemoglobin result may have several possible causes.",
                "metadata": {
                    "file_name": "hemoglobin.md",
                },
                "distance": 0.4,
            }
        ]
    }

    context = build_report_context(
        results,
        retrieved_knowledge,
    )

    assert "Test: hemoglobin" in context
    assert "Result: 11.2 g/dL" in context
    assert "Status: low" in context
    assert "hemoglobin.md" in context
    assert "Reference range: 12.0 - 15.0" in context

    # Normal results should not appear in the context.
    assert "wbc_count" not in context