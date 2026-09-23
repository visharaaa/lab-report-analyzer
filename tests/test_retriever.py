from app.models.schemas import LabResult
from app.rag.retriever import (
    build_result_query,
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

    assert query == "hemoglobin low"

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