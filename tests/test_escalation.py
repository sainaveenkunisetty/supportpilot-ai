
from agent.escalation import create_escalation


def test_escalation_has_required_fields():
    case = create_escalation("human_escalation")

    assert case["case_id"]
    assert case["reason"] == "human_escalation"
    assert case["status"] == "pending_human_review"
    assert case["created_at"]


def test_escalation_does_not_store_customer_message():
    case = create_escalation("insufficient_evidence")

    assert "customer_message" not in case
    assert "password" not in case


def test_unknown_reason_is_restricted():
    case = create_escalation("some_unknown_reason")

    assert case["reason"] == "unresolved_issue"
