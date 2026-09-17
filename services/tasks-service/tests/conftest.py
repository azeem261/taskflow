import os

os.environ.setdefault("TASKS_DATABASE_URL", "sqlite:///:memory:")

import fakeredis
import pytest
from fastapi.testclient import TestClient

from app.auth import get_current_owner
from app.database import Base, engine
from app.main import app


@pytest.fixture()
def fake_redis():
    return fakeredis.FakeStrictRedis()


@pytest.fixture()
def client(fake_redis, monkeypatch):
    Base.metadata.create_all(bind=engine)

    def override_get_current_owner():
        return "alice@example.com"

    monkeypatch.setattr("app.redis_client.get_redis", lambda: fake_redis)

    app.dependency_overrides[get_current_owner] = override_get_current_owner
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
