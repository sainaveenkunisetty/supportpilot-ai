
import json
import logging
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "supportpilot_events.jsonl"

logger = logging.getLogger("supportpilot")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    logger.addHandler(handler)


ALLOWED_EVENTS = {
    "request_checked",
    "answer_generated",
    "request_refused",
    "escalation_created",
    "model_error",
}


def log_event(event, status):
    if event not in ALLOWED_EVENTS:
        event = "request_checked"

    if status not in {"success", "refused", "failed", "pending"}:
        status = "failed"

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "status": status,
    }

    logger.info(json.dumps(record))
