CREATE OR REPLACE VIEW vw_ipca_tendencia_mm12 AS
SELECT
    date,
    indice,
    AVG(indice) OVER (
        ORDER BY date
        ROWS BETWEEN 11 PRECEDING AND CURRENT ROW
    ) AS ipca_mm12
FROM bcb.ipca
ORDER BY date;
