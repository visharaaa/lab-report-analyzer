from app.rag.report_retrieval import (
    build_report_llm_context,
    retrieve_report_knowledge,
)


def test_retrieve_report_knowledge():
    retrieved = retrieve_report_knowledge(
        "data/sample_reports/sample_report.txt",
        persist_directory="data/chroma",
        n_results=3,
    )

    expected_abnormal_results = {
        "hemoglobin",
        "hematocrit",
        "mch",
        "fasting_blood_glucose",
        "hba1c",
    }

    assert set(retrieved.keys()) == expected_abnormal_results

    for results in retrieved.values():
        assert len(results) == 3

        for result in results:
            assert "content" in result
            assert "metadata" in result
            assert "distance" in result


def test_build_report_llm_context():
    context = build_report_llm_context(
        "data/sample_reports/sample_report.txt",
        persist_directory="data/chroma",
        n_results=3,
    )

    assert "Test: hemoglobin" in context
    assert "Test: hematocrit" in context
    assert "Test: mch" in context
    assert "Test: fasting_blood_glucose" in context
    assert "Test: hba1c" in context

    assert "Status: low" in context
    assert "Status: high" in context

    # Normal results should not be included.
    assert "Test: wbc_count" not in context