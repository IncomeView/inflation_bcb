PYTHON=python

run-all:
	$(PYTHON) -m src.pipelines.run_all

ipca-geral:
	$(PYTHON) -m src.pipelines.ipca.geral

ipca-grupos:
	$(PYTHON) -m src.pipelines.ipca.grupos

ipca-subgrupos:
	$(PYTHON) -m src.pipelines.ipca.subgrupos

ipca-itens:
	$(PYTHON) -m src.pipelines.ipca.itens

ipca-subitens:
	$(PYTHON) -m src.pipelines.ipca.subitens

ipca-subitens_detalhados:
	$(PYTHON) -m src.pipelines.ipca.subitens_detalhados


run-ipca:
	$(PYTHON) -m src.pipelines.ipca.geral
	$(PYTHON) -m src.pipelines.ipca.grupos
	$(PYTHON) -m src.pipelines.ipca.subgrupos
	$(PYTHON) -m src.pipelines.ipca.itens
	$(PYTHON) -m src.pipelines.ipca.subitens
	$(PYTHON) -m src.pipelines.ipca.subitens_detalhados

selic-meta:
	$(PYTHON) -m src.pipelines.selic_meta

selic-over:
	$(PYTHON) -m src.pipelines.selic_over

run-selic:
	$(PYTHON) -m src.pipelines.selic_meta
	$(PYTHON) -m src.pipelines.selic_over