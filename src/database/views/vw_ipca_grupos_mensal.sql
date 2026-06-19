CREATE OR REPLACE VIEW vw_ipca_grupos_mensal AS
SELECT
    date,
    category,
    category_name,
    indice AS ipca_mensal,
    peso
FROM bcb.ipca_grupos
ORDER BY date, category;
