import json
import logging

import redis
from sqlalchemy.orm import Session

from app.config import settings
from app.models import StatusCount

logger = logging.getLogger("analytics")


def apply_event(db: Session, event: dict) -> None:
    task = event.get("task", {})
    status = task.get("status")
    if not status:
        return

    row = db.get(StatusCount, status)
    if row is None:
        row = StatusCount(status=status, count=0)
        db.add(row)
    row.count += 1
    db.commit()


def listen(redis_client: redis.Redis, session_factory) -> None:
    pubsub = redis_client.pubsub()
    pubsub.subscribe(settings.task_events_channel)
    for message in pubsub.listen():
        if message["type"] != "message":
            continue
        try:
            event = json.loads(message["data"])
        except (TypeError, json.JSONDecodeError):
            logger.warning("Dropping malformed task event: %r", message["data"])
            continue

        db = session_factory()
        try:
            apply_event(db, event)
        finally:
            db.close()
