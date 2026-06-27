-- 1. Total Market Cap
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_total_market_cap`
AS

SELECT
    SUM(market_cap) AS total_market_cap
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`;
-- 2. Total Trading Volume
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_total_trading_volume`
AS

SELECT
    SUM(total_volume) AS total_trading_volume
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`;
-- 3. Average Coin Price
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_average_coin_price`
AS

SELECT
    AVG(current_price) AS average_coin_price
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`;
-- 4. Top Market Cap
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_top_market_cap`
AS

SELECT
    coin_name,
    market_cap
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`
ORDER BY market_cap DESC
LIMIT 10;
-- 5. Top Trading Volume
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_top_trading_volume`
AS

SELECT
    coin_name,
    total_volume
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`
ORDER BY total_volume DESC
LIMIT 10;
-- 6. Top Gainers
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_top_gainers`
AS

SELECT
    coin_name,
    price_change_percentage_24h
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`
ORDER BY price_change_percentage_24h DESC
LIMIT 10;
-- 7. Top Losers
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_top_losers`
AS

SELECT
    coin_name,
    price_change_percentage_24h
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`
ORDER BY price_change_percentage_24h ASC
LIMIT 10;
-- 8. Average Price by Market Cap Rank
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_average_price_by_rank`
AS

SELECT
    market_cap_rank,
    AVG(current_price) AS average_price
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`
GROUP BY market_cap_rank;
-- 9. Market Cap Distribution
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_market_cap_distribution`
AS

SELECT
    market_cap_rank,
    SUM(market_cap) AS total_market_cap
FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`
GROUP BY market_cap_rank;
-- Bonus (Sangat Bagus untuk Dashboard)
CREATE OR REPLACE VIEW
`financial-market-analytics-54.market_analytics.vw_daily_market_summary`
AS

SELECT

    date,

    COUNT(DISTINCT coin_id) AS total_coins,

    SUM(market_cap) AS total_market_cap,

    SUM(total_volume) AS total_trading_volume,

    AVG(current_price) AS average_price

FROM
`financial-market-analytics-54.market_analytics.vw_market_summary`

GROUP BY date;