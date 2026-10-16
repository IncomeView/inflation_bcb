include .env
export

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


run-ipca:
	$(PYTHON) -m src.pipelines.ipca.geral
	$(PYTHON) -m src.pipelines.ipca.grupos
	$(PYTHON) -m src.pipelines.ipca.subgrupos
	$(PYTHON) -m src.pipelines.ipca.itens
	$(PYTHON) -m src.pipelines.ipca.subitens

selic-meta:
	$(PYTHON) -m src.pipelines.selic_meta

selic-over:
	$(PYTHON) -m src.pipelines.selic_over

run-selic:
	$(PYTHON) -m src.pipelines.selic_meta
	$(PYTHON) -m src.pipelines.selic_over

run-views:
	psql -U $(DB_USER) -d $(DB_NAME) -f src/database/migrations/002_create_views.sql

run-tables:
	psql -U $(DB_USER) -d $(DB_NAME) -f src/database/migrations/001_create_tables.sql

run-taxonomia:
	$(PYTHON) -m src.pipelines.ipca.taxonomia