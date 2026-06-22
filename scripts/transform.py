import pandas as pd
from datetime import datetime
import json

RAW_FILE = "data/raw/market_data.json"

OUTPUT_FILE = (
    "data/processed/market_data_clean.csv"
)


def load_json():

    with open(
        RAW_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data


def transform_data(data):

    records = []

    extraction_date = (
        datetime.now().date()
    )

    for coin in data:

        records.append({
            "coin_id":
                coin.get("id"),

            "symbol":
                coin.get("symbol"),

            "coin_name":
                coin.get("name"),

            "current_price":
                coin.get("current_price"),

            "market_cap":
                coin.get("market_cap"),

            "market_cap_rank":
                coin.get("market_cap_rank"),

            "total_volume":
                coin.get("total_volume"),

            "high_24h":
                coin.get("high_24h"),

            "low_24h":
                coin.get("low_24h"),

            "price_change_percentage_24h":
                coin.get(
                    "price_change_percentage_24h"
                ),

            "circulating_supply":
                coin.get(
                    "circulating_supply"
                ),

            "last_updated":
                coin.get(
                    "last_updated"
                ),

            "extraction_date":
                extraction_date
        })

    df = pd.DataFrame(records)

    return df


def clean_data(df):

    df = df.drop_duplicates()

    df = df.dropna(
        subset=[
            "coin_id",
            "current_price",
            "market_cap"
        ]
    )

    numeric_columns = [

        "current_price",

        "market_cap",

        "market_cap_rank",

        "total_volume",

        "high_24h",

        "low_24h",

        "price_change_percentage_24h",

        "circulating_supply"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df = df[
        (df["current_price"] > 0)
        &
        (df["market_cap"] > 0)
    ]

    return df


def save_data(df):

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )


def main():

    print(
        "Loading raw JSON..."
    )

    data = load_json()

    print(
        "Transforming data..."
    )

    df = transform_data(data)

    print(
        "Cleaning data..."
    )

    df = clean_data(df)

    save_data(df)

    print(
        f"Successfully saved "
        f"{len(df)} records"
    )


if __name__ == "__main__":
    main()