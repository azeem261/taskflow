import json
import time

import fakeredis

from app.store import notifications
from app.subscriber import start_background_listener


def test_listener_records_published_task_events():
    notifications.clear()
    fake_redis = fakeredis.FakeStrictRedis()

    start_background_listener(fake_redis)
    time.sleep(0.1)  # let the background thread subscribe

    fake_redis.publish(
        "task-events", json.dumps({"event": "task.created", "task": {"id": 1, "title": "Demo"}})
    )
    time.sleep(0.1)

    assert len(notifications) == 1
    assert notifications[0]["event"] == "task.created"


def test_listener_ignores_malformed_payloads():
    notifications.clear()
    fake_redis = fakeredis.FakeStrictRedis()

    start_background_listener(fake_redis)
    time.sleep(0.1)

    fake_redis.publish("task-events", "not-json")
    time.sleep(0.1)

    assert notifications == []
