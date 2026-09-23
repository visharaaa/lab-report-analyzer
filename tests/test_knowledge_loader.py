from app.rag.knowledge_loader import load_knowledge_base


def test_load_knowledge_base():
    documents = load_knowledge_base("knowledge_base")

    assert len(documents) == 18

    for document in documents:
        assert "file_name" in document
        assert "file_path" in document
        assert "content" in document
        assert document["content"].strip() != ""


def test_knowledge_base_contains_expected_documents():
    documents = load_knowledge_base("knowledge_base")

    file_names = {
        document["file_name"]
        for document in documents
    }

    assert "hemoglobin.md" in file_names
    assert "fasting_blood_glucose.md" in file_names
    assert "hba1c.md" in file_names