
from datetime import datetime, timezone
from uuid import uuid4


def create_escalation(reason):
    allowed_reasons = {
        "human_escalation",
        "insufficient_evidence",
        "unresolved_issue",
        "model_error",
    }

    if reason not in allowed_reasons:
        reason = "unresolved_issue"

    return {
        "case_id": str(uuid4()),
        "reason": reason,
        "status": "pending_human_review",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
