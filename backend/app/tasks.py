from .celery_app import celery_app
from .logger import logger
@celery_app.task
def process_csv_data(data):
    logger.info(f"Processing CSV data: {data}")
    return {"status": "success"}