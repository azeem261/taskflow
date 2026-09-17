import logging

logger = logging.getLogger("notifications")

notifications: list[dict] = []


def record_event(event: dict) -> None:
    notifications.append(event)
    logger.info("Received task event: %s", event)
