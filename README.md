# 🌎 Inflation Analytics – Brasil
### Macroeconomic Analytics • Inflation Intelligence • Data Engineering • Economic Modeling

>Este projeto demonstra a construção de uma plataforma analítica
de inflação brasileira, desde a coleta dos dados oficiais até a
modelagem estatística e machine learning para previsão e interpretação
das dinâmicas inflacionárias.

<br>

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=plastic&logo=python&logoColor=white)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=plastic&logo=postgresql&logoColor=white)]()
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Database-D71F00?style=plastic)]()
[![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=plastic&logo=pandas&logoColor=white)]()  
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=plastic&logo=docker&logoColor=white)]()
[![Makefile](https://img.shields.io/badge/Makefile-Automation-427819?style=plastic)]()
[![Quarto](https://img.shields.io/badge/Quarto-Reports-39729E?style=plastic)]()
[![Superset](https://img.shields.io/badge/Superset-Dashboards-20A6C9?style=plastic)]()  
[![Black](https://img.shields.io/badge/Black-Formatter-000000?style=plastic&logo=python&logoColor=white)]()
[![Ruff](https://img.shields.io/badge/Ruff-Linter-D00000?style=plastic)]()
[![PyTest](https://img.shields.io/badge/PyTest-Tested-0A9EDC?style=plastic&logo=pytest&logoColor=white)]()
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=plastic&logo=githubactions&logoColor=white)]()  
[![IBGE SIDRA](https://img.shields.io/badge/IBGE-SIDRA-2E8B57?style=plastic)]()
[![BCB SGS](https://img.shields.io/badge/BCB-SGS-F28C28?style=plastic)]()  

<br>


## 🚀 Highlights

✅ Coleta automatizada de dados do IBGE/SIDRA  
✅ Plataforma de Analytics Macroeconômico  
✅ Banco analítico PostgreSQL  
✅ Taxonomia econômica proprietária  
✅ Pipeline reprodutível de inflação e juros  
✅ Indicadores avançados de dinâmica inflacionária  
✅ Pipeline completo para Forecasting e Machine Learning  
✅ Observabilidade operacional (Audit + Health Check)  
✅ CI/CD e testes automatizados  
✅ Documentação técnica, operacional e econômica

* **Este projeto fo desenvolvido para demonstrar competências em:**

    - Engenharia de Dados
    - Analytics
    - Ciência de Dados
    - Econometria
    - Machine Learning
    - Macroeconomia Aplicada
    - Arquitetura de Dados

<br>


## Plataforma Analítica de Inflação Brasileira

Projeto de engenharia de dados, macroeconomia aplicada e analytics desenvolvido para transformar dados públicos do IBGE e Banco Central em inteligência econômica reutilizável.

O objetivo não é apenas reproduzir indicadores oficiais, mas construir uma camada analítica capaz de responder:

- Quanto foi a inflação?
- Onde ocorreram as pressões inflacionárias?
- Como a inflação se espalha pela economia?
- Quais grupos impactam mais o orçamento das famílias?
- Qual a participação de serviços, bens industriais e preços monitorados?
- Como a inflação evolui em relação à política monetária?

<br>

## 📊 Problema de Negócio

Os indicadores econômicos oficiais são públicos, mas normalmente estão fragmentados entre diferentes fontes e formatos.

Este projeto integra:

- Banco Central do Brasil (SGS)
- IBGE / SIDRA
- PostgreSQL
- Relatórios Analíticos
- Dashboards
- Estudos Econômicos

em um fluxo único capaz de produzir inteligência analítica sobre a inflação brasileira.


<br>

## 🏗 Arquitetura

```text
         ┌───────────────────────┐
         │     IBGE / SIDRA      │
         └──────────┬────────────┘
                    │
                    ▼
                 src/api
                    │
                    ▼
              src/pipelines
                    │
                    ▼
                PostgreSQL
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
             
  Views          Quarto          Superset
Analíticas     Relatórios       Dashboards
             
                    │
                    ▼
             
            Inflation Analytics
```

<br>

## 🧠 Capacidades Analíticas

O projeto evolui da coleta de dados para análises econômicas em múltiplos níveis.

- **Inflação**
    - IPCA Geral
    - Grupos
    - Subgrupos
    - Itens
    - Subitens

- **Decomposição**
    - Reconstrução do IPCA
    - Contribuição
    - Impacto
    - Hierarquia completa

- **Dinâmica Inflacionária**
    - Difusão
    - Dispersão
    - Concentração
    - Persistência
    - Momentum
    - Pressões inflacionárias

- **Blocos Macroeconômicos**
    - Alimentação no domicílio
    - Alimentação fora do domicílio
    - Serviços
    - Bens industriais
    - Preços monitorados

- **Política Monetária**
    - SELIC Meta
    - SELIC Over
    - Correlações entre inflação e juros

<br>

## 📚 Roadmap Analítico

### Fase 1 — Construção e Estrutura

00. **Auditoria dos Dados**

01. **SELIC**

02. **IPCA Geral**
    - 02.01. IPCA por Grupos
    - 02.02. IPCA por Subgrupos
    - 02.03. IPCA por Itens
    - 02.04. IPCA por Subitens

03. **Decomposição da Inflação**

04. **Dinâmica Inflacionária**

05. **Blocos Macroeconômicos**


### Fase 2 — Política Monetária

06. **IPCA e Política Monetária**

    - Objetivos:

        - SELIC vs inflação
        - Defasagens
        - Impacto dos juros
        - Transmissão monetária
        - Relação juros-preços


### Fase 3 — Modelagem

07. **Feature Engineering**

    - Objetivos:

        - construção de features
        - lags
        - rolling windows
        - indicadores de difusão
        - indicadores macroeconômicos

08. **Baseline**

    - Objetivos:

        - previsões ingênuas
        - média histórica
        - random walk
        - benchmark para modelos

09. **Modelos Estatísticos**

    - Objetivos:

        - regressões
        - ARIMA
        - SARIMA
        - VAR
        - VECM

10. **Machine Learning**

    - Objetivos:

        - Random Forest
        - XGBoost
        - LightGBM
        - modelos híbridos

11. **Avaliação**

    - Objetivos:

        - MAE
        - RMSE
        - Backtesting
        - Comparação de modelos
        - Robustez temporal

<br>

## ⚙️ Stack Tecnológica

| Camada | Tecnologias |
|----------|----------|
| Linguagem | Python 3.12 |
| Dados | Pandas, NumPy |
| Banco | PostgreSQL, SQLAlchemy |
| APIs | IBGE SIDRA, BCB SGS |
| Visualização | Matplotlib, Seaborn |
| Relatórios | Quarto |
| Dashboard | Superset |
| Qualidade | Ruff, Black, PyTest |
| Automação | GitHub Actions |
| Infraestrutura | Docker, Docker Compose |

<br>

## 🌳 Estrutura do Projeto

```text
    src
    ├── api
    ├── config
    ├── core
    ├── database
    ├── domain
    ├── pipelines
    ├── services
    └── utils

    tests
    ├── unitários
    └── data_quality

    docs
    ├── architecture.md
    ├── data_dictionary.md
    ├── pipeline.md
    └── runbook.md
```

<br>

## 🔍 Governança e Qualidade

O projeto implementa mecanismos de proteção e validação da informação.

- **Qualidade de Código**

    - Ruff
    - Black
    - Pre-Commit

- **Testes**

    - Testes unitários
    - Testes estruturais
    - Testes de qualidade dos dados

- **Operação**

    - `validate_df()`
    - `safe_replace()`
    - `health_check()`
    - `audit()`

<br>

## 📋 Documentação

A documentação é mantida dentro do próprio repositório.

| Documento | Finalidade |
|------------|------------|
| architecture.md | arquitetura técnica |
| pipeline.md | fluxo operacional |
| data_dictionary.md | catálogo dos dados |
| runbook.md | guia operacional |

<br>

## ▶️ Como Executar

1. **Criar ambiente**

```bash
    python -m venv .venv
    source .venv/bin/activate
```

2. **Instalar dependências**

```bash
    pip install -r requirements.txt
```

3. **Configurar ambiente**

```bash
    cp .env.example .env
```

4. **Atualizar dados**

```bash
    python -m src.main
```

5. **Executar testes**

```bash
    pytest
```

6. **Executar auditoria**

```bash
    python -m src.services.audit
```

7. **Gerar relatórios**

```bash
quarto render
```

<br>

## 📈 Evolução Planejada

- **Analytics**

    - Núcleos de inflação
    - Índices de difusão avançados
    - Indicadores proprietários

- **Econometria**

    - VAR
    - VECM
    - Cointegração
    - Curva de Phillips

- **Machine Learning**

    - Forecasting de inflação
    - Modelos híbridos
    - Feature Engineering macroeconômico

- **Visualização**

    - Dashboards executivos
    - Monitoramento contínuo
    - Relatórios automáticos

<br>


## ⭐ Principais Aprendizados Demonstrados

- Arquitetura de dados em Python
- ETL e ingestão de APIs públicas
- PostgreSQL e modelagem analítica
- Automação de pipelines
- Testes e qualidade de software
- Observabilidade operacional
- Modelagem econômica
- Análise quantitativa
- Documentação técnica
- Construção de produtos analíticos

<br>

## 📌 Status

**Projeto em desenvolvimento ativo.**

Atualmente o repositório representa uma plataforma analítica para estudo da inflação brasileira, combinando engenharia de dados, modelagem econômica e analytics aplicados.  
Acredito que essa versão funciona muito melhor como portólio.


