CREATE OR REPLACE VIEW vw_ipca_subgrupos_mensal AS
SELECT
    date,
    category,
    category_name,
    indice AS ipca_mensal,
    peso
FROM bcb.ipca_subgrupos
ORDER BY date, category;
