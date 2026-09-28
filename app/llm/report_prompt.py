"""
Utilities for building LLM prompts from laboratory reports.
"""

from pathlib import Path

from app.llm.prompt_builder import (
    SYSTEM_PROMPT,
    build_explanation_prompt,
)
from app.rag.report_retrieval import build_report_llm_context


def build_report_prompt(
    file_path: str | Path,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> dict[str, str]:
    """
    Build the system and user prompts for a laboratory report.
    """

    report_context = build_report_llm_context(
        file_path,
        persist_directory=persist_directory,
        n_results=n_results,
    )

    return {
        "system_prompt": SYSTEM_PROMPT.strip(),
        "user_prompt": build_explanation_prompt(
            report_context
        ).strip(),
    }