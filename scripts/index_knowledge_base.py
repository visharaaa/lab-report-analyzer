from app.rag.index_knowledge_base import index_knowledge_base


if __name__ == "__main__":
    count = index_knowledge_base()

    print(f"Indexed {count} knowledge chunks.")