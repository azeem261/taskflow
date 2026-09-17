from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_url: str = "redis://redis:6379/0"
    task_events_channel: str = "task-events"

    class Config:
        env_prefix = "NOTIFICATIONS_"


settings = Settings()
