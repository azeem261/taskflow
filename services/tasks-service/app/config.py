from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@postgres:5432/tasks"
    jwt_secret: str = "dev-secret-change-me"
    jwt_algorithm: str = "HS256"
    redis_url: str = "redis://redis:6379/0"
    task_events_channel: str = "task-events"
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_prefix = "TASKS_"


settings = Settings()
