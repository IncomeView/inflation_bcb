/*
-----------------------------------------
VIEW IPCA GRUPOS POR SUBITENS
-----------------------------------------
*/
create or replace view bcb.vw_ipca_grupos_por_subitens as
with
subgrupo as(
	select
		left(sg.category, 1)			as grupo_id,
		sg.category 					as subgrupo_id,
		sg.category_name 				as subgrupo_nome,
		sg."date",
		sg.indice						as ipca_subgrupos,
		sg.indice * (sg.peso / 100)		as ipca_subgrupos_contribuicao
	from bcb.ipca_subgrupos sg
),
item as(
	select
		left(ii.category, 2)			as subgrupo_id,
		ii.category 					as item_id,
		ii.category_name		 		as item_nome,
		ii.date,
		ii.indice						as ipca_itens,
		ii.indice * (ii.peso / 100)		as ipca_itens_contribuicao
	from bcb.ipca_itens ii
),
subitem as(
	select
		left(si.category, 4)			as item_id,
		si.category 					as subitem_id,
		si.category_name 				as subitem_nome,
		si.date,
		si.indice						as ipca_subitens,
		si.indice * (si.peso / 100)		as ipca_subitens_contribuicao
	from bcb.ipca_subitens si
)
select
	g."date"::date,
	i.nindice							as ipca_nindice,
	i.indice							as ipca_mensal,
	g.indice							as ipca_grupos,
	sg.ipca_subgrupos, ii.ipca_itens, si.ipca_subitens,
	g.indice * (g.peso / 100)			as ipca_grupos_contribuicao,
	sg.ipca_subgrupos_contribuicao, ii.ipca_itens_contribuicao, si.ipca_subitens_contribuicao,
	g.category							as grupo_id,
	sg.subgrupo_id, ii.item_id, si.subitem_id,
	g.category_name						as grupo_nome,
	sg.subgrupo_nome, ii.item_nome, si.subitem_nome
from bcb.ipca_grupos g
left join bcb.ipca_geral i on g."date" = i."date"
left join subgrupo sg on sg."grupo_id" = g."category" and sg.date = g."date"
left join item ii on ii."subgrupo_id" = sg."subgrupo_id" and ii.date = g."date"
left join subitem si on si."item_id" = ii."item_id" and si.date = g."date"
order by g."date" desc;


/*
-----------------------------------------
VIEW BLOCOS ECONOMICOS
-----------------------------------------
*/
CREATE OR REPLACE VIEW bcb.vw_blocos_macro AS
WITH
grupo AS (
    SELECT
        g.category        AS grupo_id,
        g.category_name   AS grupo_nome
    FROM bcb.ipca_grupos g
    GROUP BY g.category, g.category_name
),
subgrupo AS (
    SELECT
        LEFT(sg.category, 1) AS grupo_id,
        sg.category          AS subgrupo_id,
        sg.category_name     AS subgrupo_nome
    FROM bcb.ipca_subgrupos sg
    GROUP BY sg.category, sg.category_name
),
item AS (
    SELECT
        LEFT(ii.category, 2) AS subgrupo_id,
        ii.category          AS item_id,
        ii.category_name     AS item_nome
    FROM bcb.ipca_itens ii
    GROUP BY ii.category, ii.category_name
),
subitem AS (
    SELECT
        LEFT(si.category, 4) AS item_id,
        si.category          AS subitem_id,
        si.category_name     AS subitem_nome
    FROM bcb.ipca_subitens si
    GROUP BY si.category, si.category_name
)
SELECT
    g.grupo_id,
    g.grupo_nome,
    sg.subgrupo_id,
    sg.subgrupo_nome,
    ii.item_id,
    ii.item_nome,
    si.subitem_id,
    si.subitem_nome
FROM grupo g
LEFT JOIN subgrupo sg ON sg.grupo_id = g.grupo_id
LEFT JOIN item ii ON ii.subgrupo_id = sg.subgrupo_id
LEFT JOIN subitem si ON si.item_id = ii.item_id
ORDER BY si.subitem_id ASC;
