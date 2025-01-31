import os
import time
from dotenv import load_dotenv
from .configuration import config
from .logger import logger,log_level
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import csv
from .tasks import process_csv_data
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info(f"Request: {request.url.path} completed in {process_time} seconds")
        return response

app = FastAPI()
app.add_middleware(LoggingMiddleware)
app.title="Manoj"

# Define Pydantic model for CSV data validation
class CSVData(BaseModel):
    Industry: str
    
    # Add more fields as needed based on your CSV structure


@app.get("/")
def check():
    logger.debug("running debug statement")
    logger.info('running infromations')
    return {"message":"running",
            "log_level_set":log_level}
# Endpoint to handle CSV file upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(description="The File must be CSV")):
    if file.filename.endswith(".csv"):
        logger.info(f"CSV File Name: {file.filename}")
        logger.debug(f"CSV File Name: {file.filename}")
        
        contents = await file.read()
        decoded = contents.decode("utf-8").splitlines()
        process_csv_data.delay(decoded)
        
        # Validate CSV data using Pydantic model
        data_list = []
        try:
            reader = csv.DictReader(decoded)
            for row in reader:
                csv_data = CSVData(**row)
                data_list.append(csv_data)
        except Exception as e:
            logger.error(f"Error parsing CSV: {e}")
            raise HTTPException(status_code=400, detail=f"Error parsing CSV: {str(e)}")

        return {"data": data_list}
    else:
        logger.error("File must be a CSV")
        raise HTTPException(status_code=400, detail="File must be a CSV")