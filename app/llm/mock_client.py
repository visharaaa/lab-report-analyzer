"""
Mock LLM client used for local development and testing.
"""


def generate_mock_explanation(
    system_prompt: str,
    user_prompt: str,
) -> str:
    """
    Generate a deterministic mock response.

    This does not make any external API request.
    """

    return (
        "This is a mock laboratory report explanation. "
        "The real LLM will generate the explanation once "
        "an API provider is configured."
    )