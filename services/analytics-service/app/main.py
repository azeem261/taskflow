import threading
from contextlib import asynccontextmanager

import redis
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.aggregator import listen
from app.config import settings
from app.database import Base, SessionLocal, engine, get_db
from app.models import StatusCount

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = redis.from_url(settings.redis_url)
    thread = threading.Thread(target=listen, args=(redis_client, SessionLocal), daemon=True)
    thread.start()
    yield


app = FastAPI(title="analytics-service", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/stats")
def stats(db: Session = Depends(get_db)):
    rows = db.query(StatusCount).all()
    return {row.status: row.count for row in rows}
