CREATE OR REPLACE VIEW vw_ipca_vs_selic AS
SELECT
    i.date,
    i.indice AS ipca_mensal,
    i.acumulado12m AS ipca_12m,
    s.value AS selic_over_diaria,
    ((1 + s.value/100) ^ 252 - 1) * 100 AS selic_over_anualizada
FROM bcb.ipca i
LEFT JOIN bcb.selic_over s
    ON s.date = i.date
ORDER BY i.date;
