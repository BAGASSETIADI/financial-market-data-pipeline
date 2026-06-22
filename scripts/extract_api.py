import json
import time
import requests

from datetime import datetime

from logger import logger

from config import (
    RAW_DATA_PATH,
    EXTRACTION_REPORT_PATH,
    MAX_RETRIES,
    REQUEST_TIMEOUT
)

API_URL = (
    "https://api.coingecko.com/api/v3/coins/markets"
)

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1,
    "sparkline": "false"
}


def fetch_market_data():

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            logger.info(
                f"API Request Attempt {attempt}"
            )

            response = requests.get(
                API_URL,
                params=PARAMS,
                timeout=REQUEST_TIMEOUT
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(
                f"Attempt {attempt} Failed: {e}"
            )

            if attempt == MAX_RETRIES:
                raise

            time.sleep(2)


def save_raw_json(data):

    with open(
        RAW_DATA_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    logger.info(
        f"Raw JSON saved -> {RAW_DATA_PATH}"
    )


def create_report(
    record_count,
    execution_time
):

    report = f"""
======================================
MARKET DATA EXTRACTION REPORT
======================================

Execution Timestamp:
{datetime.now()}

Records Extracted:
{record_count}

Execution Time (Seconds):
{execution_time:.2f}

Status:
SUCCESS

Source:
CoinGecko API
"""

    with open(
        EXTRACTION_REPORT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)


def main():

    start_time = time.time()

    logger.info(
        "Starting Market Data Extraction"
    )

    data = fetch_market_data()

    save_raw_json(data)

    execution_time = (
        time.time() - start_time
    )

    create_report(
        record_count=len(data),
        execution_time=execution_time
    )

    logger.info(
        "Extraction Completed Successfully"
    )

    print(
        f"Successfully extracted "
        f"{len(data)} records"
    )


if __name__ == "__main__":
    main()