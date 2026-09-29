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

REQUIRED_SAFETY_PHRASES = [
    "not a diagnosis",
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
        return False, issues

    response_lower = response.lower()

    for phrase in FORBIDDEN_PHRASES:
        if phrase in response_lower:
            issues.append(
                f"Response contains potentially unsafe advice: '{phrase}'."
            )

    for phrase in REQUIRED_SAFETY_PHRASES:
        if phrase not in response_lower:
            issues.append(
                f"Response is missing required safety statement: '{phrase}'."
            )

    return len(issues) == 0, issues