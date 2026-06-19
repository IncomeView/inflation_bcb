CREATE OR REPLACE VIEW vw_selic_over_diaria AS
SELECT
    date,
    value AS selic_over_diaria
FROM bcb.selic_over
ORDER BY date;

