from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@postgres:5432/analytics"
    redis_url: str = "redis://redis:6379/0"
    task_events_channel: str = "task-events"

    class Config:
        env_prefix = "ANALYTICS_"


settings = Settings()
