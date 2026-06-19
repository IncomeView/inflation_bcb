CREATE OR REPLACE VIEW vw_selic_over_anualizada AS
SELECT
    date,
    ((1 + value/100) ^ 252 - 1) * 100 AS selic_over_anualizada
FROM bcb.selic_over
ORDER BY date;
