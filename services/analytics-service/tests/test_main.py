import fakeredis
from fastapi.testclient import TestClient

import app.main as main
from app.models import StatusCount


def test_stats_endpoint_returns_counts_by_status(monkeypatch, session_factory):
    monkeypatch.setattr(main.redis, "from_url", lambda *_a, **_kw: fakeredis.FakeStrictRedis())

    seed_db = session_factory()
    seed_db.add(StatusCount(status="todo", count=3))
    seed_db.commit()
    seed_db.close()

    with TestClient(main.app) as client:
        res = client.get("/stats")

    assert res.status_code == 200
    assert res.json() == {"todo": 3}


def test_health_check(monkeypatch, session_factory):
    monkeypatch.setattr(main.redis, "from_url", lambda *_a, **_kw: fakeredis.FakeStrictRedis())
    with TestClient(main.app) as client:
        res = client.get("/health")
    assert res.status_code == 200
