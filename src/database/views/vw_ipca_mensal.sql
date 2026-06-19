CREATE OR REPLACE VIEW vw_ipca_mensal AS
SELECT
    date,
    indice AS ipca_mensal
FROM bcb.ipca
ORDER BY date;
