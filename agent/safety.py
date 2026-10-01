
import re

SENSITIVE_PATTERNS = [
    r"\bpassword\s*(?:is|:)\s*\S+",
    r"\b(?:otp|one[- ]time code)\s*(?:is|:)\s*\S+",
    r"\b\d{12,19}\b",
]


ESCALATION_TERMS = [
    "unauthorized access",
    "account hacked",
    "account was hacked",
    "my account is hacked",
    "security breach",
    "legal action",
    "threatening",
    "human support",
    "speak to a person",
]


UNSUPPORTED_ACTION_TERMS = [
    "bypass authentication",
    "steal credentials",
    "reveal another customer's",
    "delete customer records",
]


def check_request(message):
    text = message.lower()

    if any(
        re.search(pattern, message, re.IGNORECASE)
        for pattern in SENSITIVE_PATTERNS
    ):
        return {
            "allowed": False,
            "reason": "sensitive_input",
            "message": (
                "Please do not share passwords, verification codes, "
                "or payment details. Remove sensitive information "
                "and submit your question again."
            ),
        }

    if any(term in text for term in UNSUPPORTED_ACTION_TERMS):
        return {
            "allowed": False,
            "reason": "unsafe_request",
            "message": (
                "I can't help with that request. "
                "I can assist with approved troubleshooting instead."
            ),
        }

    if any(term in text for term in ESCALATION_TERMS):
        return {
            "allowed": False,
            "reason": "human_escalation",
            "message": (
                "This issue needs human support. Please contact "
                "the official support team for further assistance."
            ),
        }

    return {
        "allowed": True,
        "reason": "normal",
        "message": "",
    }
