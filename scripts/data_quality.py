import pandas as pd
from datetime import datetime

INPUT_FILE = (
    "data/processed/market_data_clean.csv"
)

REPORT_FILE = (
    "data/reports/data_quality_report.txt"
)

METRICS_FILE = (
    "data/reports/data_quality_metrics.csv"
)


def load_data():

    return pd.read_csv(INPUT_FILE)


def calculate_metrics(df):

    total_records = len(df)

    duplicate_records = (
        df.duplicated().sum()
    )

    missing_values = (
        df.isnull().sum().sum()
    )

    invalid_prices = (
        df["current_price"] <= 0
    ).sum()

    invalid_market_caps = (
        df["market_cap"] <= 0
    ).sum()

    null_percentage = round(
        (
            df.isnull().sum().sum()
            /
            (df.shape[0] * df.shape[1])
        ) * 100,
        2
    )

    final_valid_records = len(
        df[
            (df["current_price"] > 0)
            &
            (df["market_cap"] > 0)
        ]
    )

    return {
        "report_date":
            datetime.now(),

        "total_records":
            total_records,

        "duplicate_records":
            duplicate_records,

        "missing_values":
            missing_values,

        "null_percentage":
            null_percentage,

        "invalid_prices":
            invalid_prices,

        "invalid_market_caps":
            invalid_market_caps,

        "final_valid_records":
            final_valid_records
    }


def save_report(metrics):

    report = f"""
=================================
DATA QUALITY REPORT
=================================

Report Date:
{metrics['report_date']}

Total Records:
{metrics['total_records']}

Missing Values:
{metrics['missing_values']}

Duplicate Records:
{metrics['duplicate_records']}

Null Percentage:
{metrics['null_percentage']} %

Invalid Prices:
{metrics['invalid_prices']}

Invalid Market Caps:
{metrics['invalid_market_caps']}

Final Valid Records:
{metrics['final_valid_records']}
"""

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)


def save_metrics(metrics):

    metrics_df = pd.DataFrame(
        [metrics]
    )

    metrics_df.to_csv(
        METRICS_FILE,
        index=False
    )


def main():

    print(
        "Running Data Quality Checks..."
    )

    df = load_data()

    metrics = calculate_metrics(df)

    save_report(metrics)

    save_metrics(metrics)

    print(
        "Data Quality Report Generated"
    )


if __name__ == "__main__":
    main()