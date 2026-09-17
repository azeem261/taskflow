import os

os.environ.setdefault("ANALYTICS_DATABASE_URL", "sqlite:///:memory:")

import pytest

from app.database import Base, SessionLocal, engine


@pytest.fixture()
def session_factory():
    Base.metadata.create_all(bind=engine)
    yield SessionLocal
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db(session_factory):
    session = session_factory()
    try:
        yield session
    finally:
        session.close()
