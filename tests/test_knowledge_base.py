
from agent.knowledge_base import KnowledgeBase


def test_login_question_finds_relevant_document():
    kb = KnowledgeBase()

    results = kb.search(
        "I cannot log in to my account"
    )

    assert len(results) > 0
    assert any(
        "Login troubleshooting" in item["text"]
        for item in results
    )


def test_unrelated_question_returns_no_documents():
    kb = KnowledgeBase()

    results = kb.search(
        "What is the weather forecast for tomorrow?"
    )

    assert results == []


def test_empty_question_returns_no_documents():
    kb = KnowledgeBase()

    assert kb.search("") == []
    assert kb.search("   ") == []
