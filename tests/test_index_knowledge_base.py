from app.rag.index_knowledge_base import index_knowledge_base


def test_index_knowledge_base(tmp_path):
    count = index_knowledge_base(
        knowledge_base_path="knowledge_base",
        persist_directory=tmp_path / "chroma",
    )

    assert count > 18