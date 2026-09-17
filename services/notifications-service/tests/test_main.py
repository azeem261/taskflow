import fakeredis
from fastapi.testclient import TestClient

import app.main as main
from app.store import notifications


def test_get_notifications_returns_recorded_events(monkeypatch):
    monkeypatch.setattr(main.redis, "from_url", lambda *_a, **_kw: fakeredis.FakeStrictRedis())
    notifications.clear()
    notifications.append({"event": "task.created", "task": {"id": 1}})

    with TestClient(main.app) as client:
        res = client.get("/notifications")

    assert res.status_code == 200
    assert res.json() == [{"event": "task.created", "task": {"id": 1}}]


def test_health_check(monkeypatch):
    monkeypatch.setattr(main.redis, "from_url", lambda *_a, **_kw: fakeredis.FakeStrictRedis())
    with TestClient(main.app) as client:
        res = client.get("/health")
    assert res.status_code == 200
