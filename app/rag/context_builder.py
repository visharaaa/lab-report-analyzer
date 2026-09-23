"""
Utilities for building LLM-ready context from retrieved
medical knowledge.
"""

from app.models.schemas import LabResult


def build_result_context(
    result: LabResult,
    retrieved_chunks: list[dict],
) -> str:
    """
    Build LLM-ready context for a single laboratory result.
    """

    test_name = result.canonical_name or result.test_name

    lines = [
        f"Test: {test_name}",
        f"Result: {result.value} {result.unit or ''}".strip(),
        f"Status: {result.flag or 'unknown'}",
        "",
        "Relevant medical information:",
    ]

    for index, chunk in enumerate(retrieved_chunks, start=1):
        source = chunk["metadata"]["file_name"]

        lines.extend(
            [
                f"\n[Source {index}: {source}]",
                chunk["content"],
            ]
        )

    return "\n".join(lines)

def build_report_context(
    results: list[LabResult],
    retrieved_knowledge: dict[str, list[dict]],
) -> str:
    """
    Build LLM-ready context for all abnormal laboratory results
    in a report.
    """

    contexts = []

    for result in results:
        if result.flag not in {"low", "high"}:
            continue

        test_name = result.canonical_name or result.test_name

        chunks = retrieved_knowledge.get(
            test_name,
            [],
        )

        if not chunks:
            continue

        context = build_result_context(
            result,
            chunks,
        )

        contexts.append(context)

    return "\n\n".join(contexts)