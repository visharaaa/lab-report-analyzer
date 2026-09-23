from app.rag.report_retrieval import retrieve_report_knowledge


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