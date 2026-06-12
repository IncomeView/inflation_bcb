CREATE TABLE bcb.calendar AS
WITH RECURSIVE dates AS (
    SELECT DATE '1980-01-01' AS date
    UNION ALL
    SELECT (date + INTERVAL '1 day')::date
    FROM dates
    WHERE date < DATE '2065-12-31'
)
SELECT
    date,
    EXTRACT(YEAR FROM date)::int AS year,
    EXTRACT(MONTH FROM date)::int AS month,
    TO_CHAR(date, 'Month') AS month_name,
    TO_CHAR(date, 'Mon') AS month_short,
    EXTRACT(DAY FROM date)::int AS day,
    EXTRACT(DOY FROM date)::int AS day_of_year,
    EXTRACT(WEEK FROM date)::int AS week_number,
    EXTRACT(QUARTER FROM date)::int AS quarter,
    'Q' || EXTRACT(QUARTER FROM date)::int AS quarter_name,
    TO_CHAR(date, 'YYYY-MM') AS year_month,
    CASE WHEN EXTRACT(ISODOW FROM date) IN (6,7) THEN TRUE ELSE FALSE END AS is_weekend
FROM dates;
