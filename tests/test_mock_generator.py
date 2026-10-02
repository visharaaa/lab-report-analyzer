from app.llm import mock_generator


def test_generate_mock_report_explanation():
    response = mock_generator.generate_mock_report_explanation(
        "data/sample_reports/sample_report.txt",
        persist_directory="data/chroma",
        n_results=3,
    )

    assert "Mock laboratory report explanation" in response
    assert "not a diagnosis" in response