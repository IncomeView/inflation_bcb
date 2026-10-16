/*
-----------------------------------------
VIEW IPCA GRUPOS POR SUBITENS
-----------------------------------------
*/
create or replace view bcb.vw_ipca_grupos_por_subitens as
with
subgrupo as(
	select
		left(sg.categoria, 1)			as grupo_id,
		sg.categoria 					as subgrupo_id,
		sg.categoria_nome 				as subgrupo_nome,
		sg."date",
		sg.indice						as ipca_subgrupos,
		sg.indice * (sg.peso / 100)		as ipca_subgrupos_contribuicao
	from bcb.ipca_subgrupos sg
),
item as(
	select
		left(ii.categoria, 2)			as subgrupo_id,
		ii.categoria 					as item_id,
		ii.categoria_nome		 		as item_nome,
		ii.date,
		ii.indice						as ipca_itens,
		ii.indice * (ii.peso / 100)		as ipca_itens_contribuicao
	from bcb.ipca_itens ii
),
subitem as(
	select
		left(si.categoria, 4)			as item_id,
		si.categoria 					as subitem_id,
		si.categoria_nome 				as subitem_nome,
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
	g.categoria							as grupo_id,
	sg.subgrupo_id, ii.item_id, si.subitem_id,
	g.categoria_nome						as grupo_nome,
	sg.subgrupo_nome, ii.item_nome, si.subitem_nome
from bcb.ipca_grupos g
left join bcb.ipca_geral i on g."date" = i."date"
left join subgrupo sg on sg."grupo_id" = g."categoria" and sg.date = g."date"
left join item ii on ii."subgrupo_id" = sg."subgrupo_id" and ii.date = g."date"
left join subitem si on si."item_id" = ii."item_id" and si.date = g."date"
order by g."date" desc;


/*
-----------------------------------------
VIEW BLOCOS ECONOMICOS
-----------------------------------------
*/
CREATE OR REPLACE VIEW bcb.vw_ipca_hierarquia AS
WITH
grupo AS (
    SELECT
        g.categoria        AS grupo_id,
        g.categoria_nome   AS grupo_nome
    FROM bcb.ipca_grupos g
    GROUP BY g.categoria, g.categoria_nome
),
subgrupo AS (
    SELECT
        LEFT(sg.categoria, 1) AS grupo_id,
        sg.categoria          AS subgrupo_id,
        sg.categoria_nome     AS subgrupo_nome
    FROM bcb.ipca_subgrupos sg
    GROUP BY sg.categoria, sg.categoria_nome
),
item AS (
    SELECT
        LEFT(ii.categoria, 2) AS subgrupo_id,
        ii.categoria          AS item_id,
        ii.categoria_nome     AS item_nome
    FROM bcb.ipca_itens ii
    GROUP BY ii.categoria, ii.categoria_nome
),
subitem AS (
    SELECT
        LEFT(si.categoria, 4) AS item_id,
        si.categoria          AS subitem_id,
        si.categoria_nome     AS subitem_nome
    FROM bcb.ipca_subitens si
    GROUP BY si.categoria, si.categoria_nome
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


/*
-----------------------------------------
VIEW IPCA TAXONOMIA MACRO
-----------------------------------------
*/
CREATE OR REPLACE VIEW bcb.vw_ipca_taxonomia AS
SELECT
    h.grupo_id,
    h.grupo_nome,
    h.subgrupo_id,
    h.subgrupo_nome,
    h.item_id,
    h.item_nome,
    h.subitem_id,
    h.subitem_nome,
    c.bloco_macro,
    c.sub_bloco,
    c.categoria_cidada,
    c.subcategoria_cidada
FROM bcb.vw_ipca_hierarquia h
LEFT JOIN bcb.ipca_taxonomia c
    ON h.subitem_id = c.subitem_id;
