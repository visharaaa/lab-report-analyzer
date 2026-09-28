"""
Utilities for validating generated laboratory report explanations.
"""


FORBIDDEN_PHRASES = [
    "you should take",
    "you need to take",
    "start taking",
    "stop taking",
    "increase your dose",
    "decrease your dose",
]


def validate_response(response: str) -> tuple[bool, list[str]]:
    """
    Validate an LLM-generated laboratory report explanation.

    Returns:
        A tuple containing:
        - whether the response passed validation
        - a list of validation issues
    """

    issues = []

    if not response.strip():
        issues.append("Response is empty.")

    response_lower = response.lower()

    for phrase in FORBIDDEN_PHRASES:
        if phrase in response_lower:
            issues.append(
                f"Response contains potentially unsafe advice: '{phrase}'."
            )

    return len(issues) == 0, issues