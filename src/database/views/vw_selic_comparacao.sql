CREATE OR REPLACE VIEW vw_selic_comparacao AS
SELECT
    o.date,
    o.value AS selic_over_diaria,
    ((1 + o.value/100) ^ 252 - 1) * 100 AS selic_over_anualizada,
    m.value AS selic_meta_anual
FROM bcb.selic_over o
LEFT JOIN bcb.selic_meta m
    ON m.date = o.date
ORDER BY o.date;
