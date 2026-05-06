create or replace view "vw_listCategories" as
with
grupo as(
	select
		g.category			as "idGrupos",
		g.category_name 	as grupos
	from bcb.ipca_grupos g
	group by g.category, g.category_name 
),
subgrupo as(
	select
		left(sg.category, 1)	as "idGrupos",
		sg.category 			as "idSubGrupos",
		sg.category_name 		as "subGrupos"
	from bcb.ipca_subgrupos sg
	group by sg.category, sg.category_name
),
item as(
	select
		left(ii.category, 2)	as "idSubGrupos",
		ii.category 			as "idItens",
		ii.category_name 		as itens
	from bcb.ipca_itens ii
	group by ii.category, ii.category_name 
),
subitem as(
	select
		left(si.category, 4)	as "idItens",
		si.category 			as "idSubItens",
		si.category_name 		as "subItens"
	from bcb.ipca_subitens si
	group by si.category, si.category_name 
)
select
	g."idGrupos", g.grupos,
	sg."idSubGrupos", sg."subGrupos",
	ii."idItens",ii.itens,
	si."idSubItens", si."subItens" 
from grupo g
left join subgrupo sg on sg."idGrupos" = g."idGrupos" 
left join item ii on ii."idSubGrupos" = sg."idSubGrupos" 
left join subitem si on si."idItens" = ii."idItens"
order by si."idSubItens" asc;
