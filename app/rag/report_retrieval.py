"""
High-level utilities for retrieving medical knowledge
and building LLM-ready context from a laboratory report.
"""

from pathlib import Path

from app.document_processing.pipeline import process_report
from app.rag.context_builder import build_report_context
from app.rag.retriever import retrieve_for_report


def retrieve_report_knowledge(
    file_path: str | Path,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> dict[str, list[dict]]:
    """
    Process a laboratory report and retrieve relevant
    medical knowledge for its abnormal results.
    """

    results = process_report(file_path)

    return retrieve_for_report(
        results,
        persist_directory=persist_directory,
        n_results=n_results,
    )


def build_report_llm_context(
    file_path: str | Path,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> str:
    """
    Process a laboratory report, retrieve relevant medical
    knowledge, and build LLM-ready context.
    """

    results = process_report(file_path)

    retrieved_knowledge = retrieve_for_report(
        results,
        persist_directory=persist_directory,
        n_results=n_results,
    )

    return build_report_context(
        results,
        retrieved_knowledge,
    )