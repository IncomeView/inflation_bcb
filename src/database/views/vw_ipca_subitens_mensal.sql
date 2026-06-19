CREATE OR REPLACE VIEW vw_ipca_subitens_mensal AS
SELECT
    date,
    category,
    category_name,
    indice AS ipca_mensal,
    peso
FROM bcb.ipca_subitens
ORDER BY date, category;
