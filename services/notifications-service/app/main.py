from contextlib import asynccontextmanager

import redis
from fastapi import FastAPI

from app.config import settings
from app.store import notifications
from app.subscriber import start_background_listener


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = redis.from_url(settings.redis_url)
    start_background_listener(redis_client)
    yield


app = FastAPI(title="notifications-service", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/notifications")
def get_notifications():
    return notifications
