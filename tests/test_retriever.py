from app.rag.retriever import retrieve_knowledge


def test_retrieve_knowledge():
    results = retrieve_knowledge(
        "What can cause low hemoglobin?",
        persist_directory="data/chroma",
        n_results=3,
    )

    assert len(results) == 3

    for result in results:
        assert "content" in result
        assert "metadata" in result
        assert "distance" in result