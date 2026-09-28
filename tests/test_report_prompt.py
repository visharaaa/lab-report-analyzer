from app.llm.report_prompt import build_report_prompt


def test_build_report_prompt():
    prompts = build_report_prompt(
        "data/sample_reports/sample_report.txt",
        persist_directory="data/chroma",
        n_results=3,
    )

    assert "system_prompt" in prompts
    assert "user_prompt" in prompts

    assert "Do not diagnose" in prompts["system_prompt"]
    assert "Do not recommend medications" in prompts["system_prompt"]

    assert "hemoglobin" in prompts["user_prompt"]
    assert "11.2 g/dL" in prompts["user_prompt"]
    assert "12.0 - 15.0" in prompts["user_prompt"]

    assert "fasting_blood_glucose" in prompts["user_prompt"]
    assert "hba1c" in prompts["user_prompt"]