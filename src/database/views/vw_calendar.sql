CREATE OR REPLACE VIEW vw_calendar AS
SELECT
    date,
    EXTRACT(YEAR FROM date) AS ano,
    EXTRACT(MONTH FROM date) AS mes,
    EXTRACT(QUARTER FROM date) AS trimestre
FROM bcb.calendar
ORDER BY date;
