from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")

RAW_DATA_PATH = "data/raw/market_data.json"

EXTRACTION_REPORT_PATH = (
    "data/reports/extraction_summary.txt"
)

LOG_FILE = "logs/pipeline.log"

MAX_RETRIES = 3

REQUEST_TIMEOUT = 30