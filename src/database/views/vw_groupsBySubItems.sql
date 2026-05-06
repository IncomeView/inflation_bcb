create or replace view "vw_groupsBySubItems" as
with
subgrupo as(
	select
		left(sg.category, 1)			as "idGrupos",
		sg.category 					as "idSubGrupos",
		sg.category_name 				as "subGrupos",
		sg."date",
		sg.indice						as "ipcaSubGruposCheio",
		sg.indice * (sg.peso / 100)		as "ipcaSubGruposPorPeso"
	from bcb.ipca_subgrupos sg
),
item as(
	select
		left(ii.category, 2)			as "idSubGrupos",
		ii.category 					as "idItens",
		ii.category_name		 		as itens,
		ii.date,
		ii.indice						as "ipcaItensCheio",
		ii.indice * (ii.peso / 100)		as "ipcaItensPorPeso"
	from bcb.ipca_itens ii
),
subitem as(
	select
		left(si.category, 4)			as "idItens",
		si.category 					as "idSubItens",
		si.category_name 				as "subItens",
		si.date,
		si.indice						as "ipcaSubItensCheio",
		si.indice * (si.peso / 100)		as "ipcaSubItensPorPeso"
	from bcb.ipca_subitens si
)
select
	g."date"::date,
	i."nIndice"							as "ipca_nIndice",
	i.indice							as ipca,
	g.indice							as "ipcaGruposCheio",
	sg."ipcaSubGruposCheio", ii."ipcaItensCheio", si."ipcaSubItensCheio",
	g.indice * (g.peso / 100)			as "ipcaGruposPorPeso",
	sg."ipcaSubGruposPorPeso", ii."ipcaItensPorPeso", si."ipcaSubItensPorPeso",
	g.category							as "idGrupos",
	sg."idSubGrupos", ii."idItens", si."idSubItens",
	g.category_name						as grupos,
	sg."subGrupos",
	ii.itens,
	si."subItens"
from bcb.ipca_grupos g
left join bcb.ipca i on g."date" = i."date"
left join subgrupo sg on sg."idGrupos" = g."category" and sg.date = g."date"
left join item ii on ii."idSubGrupos" = sg."idSubGrupos" and ii.date = g."date"
left join subitem si on si."idItens" = ii."idItens" and si.date = g."date"
order by g."date" desc;

