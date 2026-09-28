from app.llm.prompt_builder import (
    SYSTEM_PROMPT,
    build_explanation_prompt,
)


def test_system_prompt_contains_safety_rules():
    assert "Do not diagnose" in SYSTEM_PROMPT
    assert "Do not recommend medications" in SYSTEM_PROMPT
    assert "Do not invent laboratory reference ranges" in SYSTEM_PROMPT


def test_build_explanation_prompt():
    context = """
Test: hemoglobin
Result: 11.2 g/dL
Reference range: 12.0 - 15.0
Status: low

Relevant medical information:
A low hemoglobin result may have several possible causes.
"""

    prompt = build_explanation_prompt(context)

    assert "hemoglobin" in prompt
    assert "11.2 g/dL" in prompt
    assert "12.0 - 15.0" in prompt
    assert "patient-friendly" in prompt
    assert "Do not diagnose" in prompt