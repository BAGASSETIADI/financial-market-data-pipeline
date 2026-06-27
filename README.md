# Financial Market Data Pipeline & Analytics Warehouse

## Project Overview

This project demonstrates an end-to-end Data Engineering and Analytics workflow using Python, CoinGecko API, Google BigQuery, SQL, and Looker Studio.

The objective is to build a production-style financial market data platform that automatically extracts cryptocurrency market data, performs data validation and transformation, loads data into a cloud data warehouse, implements dimensional modeling using Star Schema, and provides analytical insights through SQL and dashboards.

---

## Business Problem

Financial market data changes rapidly and originates from external APIs. Organizations require reliable pipelines to:

- Collect market data automatically
- Ensure data quality and consistency
- Store historical market information
- Support analytical reporting
- Enable business intelligence dashboards

This project simulates a real-world market analytics platform used by financial analysts and data teams.

---

## Architecture

CoinGecko API

↓

Extract Layer (Python)

↓

Raw JSON Storage

↓

Transformation Layer

↓

Data Quality Monitoring

↓

Google BigQuery

↓

Star Schema Data Warehouse

- dim_coin
- dim_date
- fact_market_data

↓

Analytics Views

↓

Looker Studio Dashboard

---

## Technology Stack

### Programming

- Python

### Libraries

- requests
- pandas
- numpy
- google-cloud-bigquery
- python-dotenv

### Cloud Platform

- Google BigQuery

### Data Visualization

- Looker Studio

### Development Tools

- VS Code
- Git
- GitHub

---

## ETL Workflow

### Extract

Data is extracted from the CoinGecko Market API.

Endpoint:

https://api.coingecko.com/api/v3/coins/markets

Parameters:

- vs_currency=usd
- order=market_cap_desc
- per_page=250
- page=1
- sparkline=false

### Transform

Transformation process includes:

- JSON parsing
- Column standardization
- Data type conversion
- Missing value handling
- Duplicate removal
- Extraction date generation

### Data Quality

Validation checks:

- Total Records
- Missing Values
- Duplicate Records
- Null Percentage
- Invalid Prices
- Invalid Market Caps
- Final Valid Records

### Load

Processed data is loaded into BigQuery as:

market_raw

---

## Data Warehouse Design

### Dimension Tables

#### dim_coin

- coin_id
- symbol
- coin_name
- market_cap_rank

#### dim_date

- date
- year
- month
- month_name
- quarter

### Fact Table

#### fact_market_data

- coin_id
- date
- current_price
- market_cap
- total_volume
- high_24h
- low_24h
- price_change_percentage_24h

---

## Analytics Layer

### Views

- vw_market_summary
- vw_total_market_cap
- vw_total_trading_volume
- vw_average_coin_price
- vw_top_market_cap
- vw_top_trading_volume
- vw_top_gainers
- vw_top_losers
- vw_average_price_by_rank
- vw_market_cap_distribution
- vw_daily_market_summary

---

## Analytical Insights

The warehouse supports:

- Total Market Capitalization
- Total Trading Volume
- Average Coin Price
- Top Market Cap Coins
- Top Trading Volume Coins
- Top Gainers
- Top Losers
- Market Cap Distribution
- Daily Market Summary

---

## Project Structure

market-data-pipeline/

├── data/

│ ├── raw/

│ ├── processed/

│ └── reports/

├── scripts/

│ ├── extract_api.py

│ ├── transform.py

│ ├── data_quality.py

│ ├── load_bigquery.py

│ └── config.py

├── sql/

│ ├── star_schema.sql

│ └── analytical_queries.sql

├── dashboard/

├── logs/

├── credentials/

├── requirements.txt

└── README.md

---

## Dashboard

Dashboard pages:

### Page 1 – Market Overview

KPIs:

- Total Market Cap
- Total Trading Volume
- Average Coin Price
- Number of Coins

### Page 2 – Market Performance

- Top Gainers
- Top Losers
- Market Cap Distribution

### Page 3 – Market Analytics

- Price Analysis
- Volume Analysis
- Market Capitalization Analysis

### Page 4 – Data Quality Monitoring

- Total Records
- Missing Values
- Duplicate Records
- Invalid Records

---

## Results

This project demonstrates practical experience in:

- REST API Integration
- ETL Pipeline Development
- Data Quality Monitoring
- Cloud Data Warehousing
- Star Schema Modeling
- SQL Analytics
- Dashboard Development
- Data Engineering Best Practices

---

## Future Improvements

- Workflow orchestration using Apache Airflow
- Incremental loading strategy
- Historical market tracking
- Automated scheduling with Cloud Functions
- CI/CD integration
- Real-time streaming pipeline
