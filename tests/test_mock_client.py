from app.llm.mock_client import generate_mock_explanation


def test_generate_mock_explanation():
    response = generate_mock_explanation(
        system_prompt="Explain safely.",
        user_prompt="Explain this laboratory result.",
    )

    assert isinstance(response, str)
    assert len(response) > 0
    assert "mock" in response.lower()