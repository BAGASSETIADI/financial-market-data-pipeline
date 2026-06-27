CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_market_summary`
AS

SELECT

    f.date,

    c.coin_id,
    c.symbol,
    c.coin_name,
    c.market_cap_rank,

    d.year,
    d.month,
    d.month_name,
    d.quarter,

    f.current_price,
    f.market_cap,
    f.total_volume,
    f.high_24h,
    f.low_24h,
    f.price_change_percentage_24h

FROM
`financial-market-analytics-54.market_analytics.fact_market_data` f

LEFT JOIN
`financial-market-analytics-54.market_analytics.dim_coin` c
ON f.coin_id = c.coin_id

LEFT JOIN
`financial-market-analytics-54.market_analytics.dim_date` d
ON f.date = d.date;