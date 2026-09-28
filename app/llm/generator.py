"""
High-level utilities for generating laboratory report explanations.
"""

from pathlib import Path

from app.llm.client import generate_explanation
from app.llm.report_prompt import build_report_prompt
from app.safety.response_validator import validate_response


def generate_report_explanation(
    file_path: str | Path,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
    model: str | None = None,
) -> str:
    """
    Generate and validate an explanation for a laboratory report.
    """

    prompts = build_report_prompt(
        file_path,
        persist_directory=persist_directory,
        n_results=n_results,
    )

    response = generate_explanation(
        system_prompt=prompts["system_prompt"],
        user_prompt=prompts["user_prompt"],
        model=model,
    )

    is_valid, issues = validate_response(response)

    if not is_valid:
        raise ValueError(
            "Generated response failed safety validation: "
            + "; ".join(issues)
        )

    return response