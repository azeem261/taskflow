FROM python:3.11-slim-bookworm AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --default-timeout=100 --retries=5 --prefix=/install -r requirements.txt

FROM python:3.11-slim-bookworm
WORKDIR /app

RUN groupadd --system --gid 1000 app \
    && useradd --system --uid 1000 --gid app --no-create-home --shell /usr/sbin/nologin app

COPY --from=builder /install /usr/local
COPY . .
RUN chown -R app:app /app

USER app
EXPOSE 8000
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
