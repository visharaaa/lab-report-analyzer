"""
Utilities for retrieving relevant medical knowledge.
"""

from app.models.schemas import LabResult
from app.rag.embeddings import (
    generate_embeddings,
    load_embedding_model,
)
from app.rag.vector_store import (
    create_vector_store,
    search_documents,
)


def retrieve_knowledge(
    query: str,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> list[dict]:
    """
    Retrieve the most relevant knowledge chunks for a query.
    """

    model = load_embedding_model()

    query_embedding = generate_embeddings(
        [query],
        model,
    )[0]

    collection = create_vector_store(
        persist_directory
    )

    return search_documents(
        collection,
        query_embedding,
        n_results=n_results,
    )


def build_result_query(result: LabResult) -> str:
    """
    Build a semantic retrieval query from a laboratory result.
    """

    test_name = result.canonical_name or result.test_name

    parts = [test_name]

    if result.flag:
        parts.append(result.flag)

    return " ".join(parts)


def retrieve_for_result(
    result: LabResult,
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> list[dict]:
    """
    Retrieve relevant medical knowledge for a laboratory result.
    """

    query = build_result_query(result)

    return retrieve_knowledge(
        query=query,
        persist_directory=persist_directory,
        n_results=n_results,
    )

def retrieve_for_report(
    results: list[LabResult],
    persist_directory: str = "data/chroma",
    n_results: int = 3,
) -> dict[str, list[dict]]:
    """
    Retrieve relevant medical knowledge for abnormal
    laboratory results in a report.
    """

    retrieved = {}

    for result in results:
        if result.flag not in {"low", "high"}:
            continue

        key = result.canonical_name or result.test_name

        retrieved[key] = retrieve_for_result(
            result,
            persist_directory=persist_directory,
            n_results=n_results,
        )

    return retrieved