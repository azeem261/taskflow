import json
import logging
import threading

import redis

from app.config import settings
from app.store import record_event

logger = logging.getLogger("notifications")


def listen(redis_client: redis.Redis) -> None:
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
        record_event(event)


def start_background_listener(redis_client: redis.Redis) -> threading.Thread:
    thread = threading.Thread(target=listen, args=(redis_client,), daemon=True)
    thread.start()
    return thread
