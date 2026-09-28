"""
High-level utilities for generating laboratory report explanations.
"""

from pathlib import Path

from app.llm.client import generate_explanation
from app.llm.report_prompt import build_report_prompt


def generate_report_explanation(
    file_path: str | Path,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
    model: str | None = None,
) -> str:
    """
    Generate an explanation for a laboratory report.

    Builds the report prompts and sends them to the configured LLM.
    """

    prompts = build_report_prompt(
        file_path,
        persist_directory=persist_directory,
        n_results=n_results,
    )

    return generate_explanation(
        system_prompt=prompts["system_prompt"],
        user_prompt=prompts["user_prompt"],
        model=model,
    )