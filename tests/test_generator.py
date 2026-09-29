import pytest

from app.llm import generator


def test_generate_report_explanation(monkeypatch):
    def fake_generate_explanation(
        system_prompt,
        user_prompt,
        model=None,
    ):
        assert "Do not diagnose" in system_prompt
        assert "hemoglobin" in user_prompt

        return (
            "This is a safe mock explanation. "
            "This explanation is not a diagnosis."
        )

    monkeypatch.setattr(
        generator,
        "generate_explanation",
        fake_generate_explanation,
    )

    response = generator.generate_report_explanation(
        "data/sample_reports/sample_report.txt",
        persist_directory="data/chroma",
        n_results=3,
    )

    assert response == (
        "This is a safe mock explanation. "
        "This explanation is not a diagnosis."
    )


def test_generate_report_explanation_rejects_unsafe_response(
    monkeypatch,
):
    def fake_generate_explanation(
        system_prompt,
        user_prompt,
        model=None,
    ):
        return (
            "You should take iron supplements. "
            "This explanation is not a diagnosis."
        )

    monkeypatch.setattr(
        generator,
        "generate_explanation",
        fake_generate_explanation,
    )

    with pytest.raises(ValueError, match="safety validation"):
        generator.generate_report_explanation(
            "data/sample_reports/sample_report.txt",
            persist_directory="data/chroma",
            n_results=3,
        )