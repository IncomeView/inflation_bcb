CREATE OR REPLACE VIEW vw_ipca_12m AS
SELECT
    date,
    acumulado12m AS ipca_12m
FROM bcb.ipca
ORDER BY date;
