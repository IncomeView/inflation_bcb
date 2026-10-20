# Arquitetura

## Objetivo

Construir uma camada analítica para inflação e juros no Brasil.

## Fontes

- Banco Central do Brasil (SGS)
- SIDRA / IBGE

## Tecnologias

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Quarto
- Superset

## Estrutura

* src/
    - ├── api
    - ├── core
    - ├── database
    - ├── domain
    - ├── pipelines
    - └── services

## Camadas

* api → Coleta
* domain → Regras econômicas
* core → Infraestrutura
* database → Persistência
* pipelines → Orquestração
* reports → Publicação