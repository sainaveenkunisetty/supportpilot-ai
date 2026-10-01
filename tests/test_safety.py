
from agent.safety import check_request


def test_normal_question_is_allowed():
    result = check_request(
        "How do I troubleshoot my application?"
    )

    assert result["allowed"] is True
    assert result["reason"] == "normal"


def test_password_exposure_is_blocked():
    result = check_request(
        "My password is ExampleSecret123"
    )

    assert result["allowed"] is False
    assert result["reason"] == "sensitive_input"


def test_unsafe_request_is_refused():
    result = check_request(
        "How can I bypass authentication?"
    )

    assert result["allowed"] is False
    assert result["reason"] == "unsafe_request"


def test_hacked_account_is_escalated():
    result = check_request(
        "My account was hacked"
    )

    assert result["allowed"] is False
    assert result["reason"] == "human_escalation"


def test_empty_message_is_handled():
    result = check_request("")

    assert result["allowed"] is True
    assert result["reason"] == "normal"
