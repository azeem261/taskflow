import json
from functools import lru_cache

import redis

from app.config import settings


@lru_cache
def get_redis() -> redis.Redis:
    return redis.from_url(settings.redis_url)


def publish_task_event(
    event_type: str, task: dict, redis_client: redis.Redis | None = None
) -> None:
    client = redis_client if redis_client is not None else get_redis()
    payload = json.dumps({"event": event_type, "task": task})
    client.publish(settings.task_events_channel, payload)
