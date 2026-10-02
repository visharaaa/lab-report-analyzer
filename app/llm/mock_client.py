"""
Mock LLM client used for local development and testing.
"""


def generate_mock_explanation(system_prompt: str, user_prompt: str) -> str:
    """
    Generate a realistic local mock explanation for testing.
    """

    return (
        "Mock laboratory report explanation:\n\n"
        "Some results are outside the laboratory reference ranges. "
        "Hemoglobin is 11.2 g/dL, which is below the reported reference "
        "range of 12-15 g/dL. Hematocrit is also below the reported range, "
        "and MCH is slightly below its reference range.\n\n"
        "Fasting blood glucose is 108 mg/dL, which is above the reference "
        "range provided in the report. HbA1c is 5.9%, which is also above "
        "the reported reference range.\n\n"
        "These results can have several possible explanations, and the "
        "results alone cannot determine the underlying cause. Additional "
        "clinical information may be needed to interpret them properly.\n\n"
        "This explanation is not a diagnosis."
    )