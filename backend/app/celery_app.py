from celery import Celery
from .configuration import config

# Initialize Celery
celery_app = Celery(
    "tasks",
    broker=config.get("celery", "broker_url",fallback='redis://localhost:6379/0'),
    backend=config.get("celery", "result_backend",fallback='redis://localhost:6379/0'),
)

celery_app.conf.update(task_serializer="json", accept_content=["json"])