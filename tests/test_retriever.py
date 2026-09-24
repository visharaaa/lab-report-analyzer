from app.models.schemas import LabResult
from app.rag.retriever import (
    build_result_query,
    retrieve_for_report,
    retrieve_for_result,
    retrieve_knowledge,
)


def test_retrieve_knowledge():
    results = retrieve_knowledge(
        "What can cause low hemoglobin?",
        persist_directory="data/chroma",
        n_results=3,
    )

    assert len(results) == 3

    for result in results:
        assert "content" in result
        assert "metadata" in result
        assert "distance" in result


def test_build_result_query():
    result = LabResult(
        test_name="Hemoglobin",
        canonical_name="hemoglobin",
        value=11.2,
        unit="g/dL",
        reference_low=12.0,
        reference_high=15.0,
        flag="low",
    )

    query = build_result_query(result)

    assert query == (
    "hemoglobin low result "
    "what it means possible causes important context"
)


def test_retrieve_for_result():
    result = LabResult(
        test_name="Hemoglobin",
        canonical_name="hemoglobin",
        value=11.2,
        unit="g/dL",
        reference_low=12.0,
        reference_high=15.0,
        flag="low",
    )

    results = retrieve_for_result(
        result,
        n_results=3,
    )

    assert len(results) == 3

    assert results[0]["metadata"]["file_name"] == "hemoglobin.md"


def test_retrieve_for_report():
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

    retrieved = retrieve_for_report(
        results,
        n_results=3,
    )

    assert "hemoglobin" in retrieved
    assert "wbc_count" not in retrieved

    assert len(retrieved["hemoglobin"]) == 3