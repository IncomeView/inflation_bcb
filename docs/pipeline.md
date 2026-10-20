# Pipeline de Dados

## Visão Geral

O projeto coleta indicadores econômicos do Banco Central e do IBGE,
estrutura os dados em PostgreSQL e disponibiliza camadas analíticas para
Quarto e Superset.

## Arquitetura

- SIDRA → api.sidra_client → pipelines.ipca → PostgreSQL
- SGS / BCB → api.sgs_series → pipelines.selic_* → PostgreSQL
- PostgreSQL → Views Analíticas → Quarto → Superset


* IPCA Geral
    -    ├─ ipca_geral
    -    ├─ ipca_grupos
    -    ├─ ipca_subgrupos
    -    ├─ ipca_itens
    -    ├─ ipca_subitens
    -    └─ ipca_taxonomia

* run_all()
    - ├─ run_ipca_geral()
    - ├─ run_ipca_grupos()
    - ├─ run_ipca_subgrupos()
    - ├─ run_ipca_itens()
    - ├─ run_ipca_subitens()
    - ├─ run_taxonomia()
    - ├─ run_selic_meta()
    - └─ run_selic_over()