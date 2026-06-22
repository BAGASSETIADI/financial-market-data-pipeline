import os
import pandas as pd

from dotenv import load_dotenv
from google.cloud import bigquery

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)

CSV_FILE = (
    "data/processed/market_data_clean.csv"
)

TABLE_NAME = "market_raw"

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = GOOGLE_APPLICATION_CREDENTIALS


def load_to_bigquery():

    client = bigquery.Client(
        project=PROJECT_ID
    )

    df = pd.read_csv(CSV_FILE)

    table_id = (
        f"{PROJECT_ID}."
        f"{DATASET_ID}."
        f"{TABLE_NAME}"
    )

    job_config = (
        bigquery.LoadJobConfig(
            write_disposition=
            "WRITE_TRUNCATE",
            autodetect=True
        )
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    print(
        f"Loaded {len(df)} rows "
        f"to {table_id}"
    )


if __name__ == "__main__":
    load_to_bigquery()