CREATE OR REPLACE VIEW vw_selic_meta_anual AS
SELECT
    date,
    value AS selic_meta_anual
FROM bcb.selic_meta
ORDER BY date;
