CREATE OR REPLACE VIEW vw_ipca_itens_mensal AS
SELECT
    date,
    category,
    category_name,
    indice AS ipca_mensal,
    peso
FROM bcb.ipca_itens
ORDER BY date, category;
