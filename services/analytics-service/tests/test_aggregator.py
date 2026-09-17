import json
import time

import fakeredis

from app.aggregator import apply_event, listen
from app.models import StatusCount


def test_apply_event_increments_status_count(db):
    apply_event(db, {"event": "task.created", "task": {"id": 1, "status": "todo"}})
    apply_event(db, {"event": "task.created", "task": {"id": 2, "status": "todo"}})
    apply_event(db, {"event": "task.updated", "task": {"id": 1, "status": "done"}})

    rows = {row.status: row.count for row in db.query(StatusCount).all()}
    assert rows == {"todo": 2, "done": 1}


def test_apply_event_ignores_events_without_status(db):
    apply_event(db, {"event": "task.created", "task": {"id": 1}})
    assert db.query(StatusCount).all() == []


def test_listen_consumes_published_events_end_to_end(session_factory):
    fake_redis = fakeredis.FakeStrictRedis()
    import threading

    thread = threading.Thread(target=listen, args=(fake_redis, session_factory), daemon=True)
    thread.start()
    time.sleep(0.1)

    fake_redis.publish(
        "task-events", json.dumps({"event": "task.created", "task": {"id": 1, "status": "todo"}})
    )
    time.sleep(0.1)

    db = session_factory()
    try:
        rows = {row.status: row.count for row in db.query(StatusCount).all()}
    finally:
        db.close()
    assert rows == {"todo": 1}


def test_listen_ignores_malformed_payload(session_factory):
    fake_redis = fakeredis.FakeStrictRedis()
    import threading

    thread = threading.Thread(target=listen, args=(fake_redis, session_factory), daemon=True)
    thread.start()
    time.sleep(0.1)

    fake_redis.publish("task-events", "not-json")
    time.sleep(0.1)

    db = session_factory()
    try:
        rows = db.query(StatusCount).all()
    finally:
        db.close()
    assert rows == []
