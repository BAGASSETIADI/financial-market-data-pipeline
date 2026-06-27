-- DIM COIN

CREATE OR REPLACE TABLE
`financial-market-analytics-54.market_analytics.dim_coin`
AS

SELECT DISTINCT

    coin_id,
    symbol,
    coin_name,
    market_cap_rank

FROM
`financial-market-analytics-54.market_analytics.market_raw`;
CREATE OR REPLACE TABLE
`financial-market-analytics-54.market_analytics.dim_date`
AS

SELECT DISTINCT

    DATE(extraction_date) AS date,

    EXTRACT(
        YEAR
        FROM DATE(extraction_date)
    ) AS year,

    EXTRACT(
        MONTH
        FROM DATE(extraction_date)
    ) AS month,

    FORMAT_DATE(
        '%B',
        DATE(extraction_date)
    ) AS month_name,

    CONCAT(
        'Q',
        CAST(
            EXTRACT(
                QUARTER
                FROM DATE(extraction_date)
            ) AS STRING
        )
    ) AS quarter

FROM
`financial-market-analytics-54.market_analytics.market_raw`;

CREATE OR REPLACE TABLE
`financial-market-analytics-54.market_analytics.fact_market_data`
AS

SELECT

    coin_id,

    DATE(extraction_date) AS date,

    current_price,

    market_cap,

    total_volume,

    high_24h,

    low_24h,

    price_change_percentage_24h

FROM
`financial-market-analytics-54.market_analytics.market_raw`;