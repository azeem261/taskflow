import pytest
from fastapi import HTTPException
from jose import jwt

from app.auth import get_current_owner
from app.config import settings


def test_get_current_owner_accepts_valid_bearer_token():
    token = jwt.encode(
        {"sub": "dave@example.com"}, settings.jwt_secret, algorithm=settings.jwt_algorithm
    )
    assert get_current_owner(authorization=f"Bearer {token}") == "dave@example.com"


def test_get_current_owner_rejects_missing_bearer_scheme():
    with pytest.raises(HTTPException) as exc_info:
        get_current_owner(authorization="not-a-bearer-token")
    assert exc_info.value.status_code == 401


def test_get_current_owner_rejects_invalid_token():
    with pytest.raises(HTTPException) as exc_info:
        get_current_owner(authorization="Bearer garbage")
    assert exc_info.value.status_code == 401
