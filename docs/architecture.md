# Arquitetura

## Fontes

- Banco Central (SGS)
- Banco Central (Meta Selic)
- SIDRA IBGE

## Pipeline

api
  ↓
pipelines
  ↓
parquet
  ↓
quarto
superset

## Camadas

api
    Coleta de dados

database
    Persistência

pipelines
    Transformação

domain
    Conceitos econômicos

services
    Regras de negócio

core
    Infra compartilhada