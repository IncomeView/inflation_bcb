## 🌎 Inflation Analytics – Brasil
IPCA • SELIC • BCB/SGS • IBGE/SIDRA • PostgreSQL • Pipelines Reprodutíveis • Notebooks Educacionais

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white)]()
[![SQL](https://img.shields.io/badge/Data%20Engineering-SQL%20Advanced-green?style=for-the-badge&logo=database&logoColor=white)]()
[![Black](https://img.shields.io/badge/Black-formatter-black?style=for-the-badge)]()
[![Ruff](https://img.shields.io/badge/Ruff-linter-red?style=for-the-badge)]()  
[![BCB SGS](https://img.shields.io/badge/BCB-SGS-orange?style=for-the-badge)]()
[![IBGE SIDRA](https://img.shields.io/badge/IBGE-SIDRA-green?style=for-the-badge)]()


<br>

## 📌 Visão Geral

Este repositório reúne engenharia de dados, macroeconomia aplicada e ciência de dados para construir uma infraestrutura completa de análise da inflação brasileira.

Ele foi projetado para:

- coletar dados oficiais do IBGE/SIDRA e BCB/SGS  
- armazenar séries históricas em PostgreSQL  
- criar pipelines reprodutíveis  
- gerar notebooks educacionais  
- construir modelos estatísticos e de machine learning  
- produzir dashboards e relatórios econômicos

<br>

## 🧭 Sumário

1. Visão Geral  
2. Arquitetura  
3. Tecnologias  
4. Estrutura do Repositório  
5. Banco de Dados  
6. APIs Integradas  
7. Pipelines  
8. Notebooks Educacionais  
9. Qualidade de Código  
10. Testes Automatizados  
11. Como Executar  
12. Roadmap  
13. Filosofia  

<br>

## 🏗 Arquitetura

Fluxo principal:

```
IBGE/SIDRA → Pipelines IPCA → PostgreSQL → Notebooks → Modelos
BCB/SGS   → Pipelines SELIC → PostgreSQL → Notebooks → Dashboards
```

Componentes:

- API Clients  
- Pipelines ETL  
- PostgreSQL  
- Notebooks analíticos  
- Modelos estatísticos e ML  
- Relatórios e dashboards  
- Testes + pre-commit  

<br>

## 🛠 Tecnologias

| Stack | Tec |
|-|-|
| **Linguagem** | $\to \qquad$ Python 3.12 |
| **Banco de Dados** | $\to \qquad$ PostgreSQL <br> $\to \qquad$ SQLAlchemy |
| **APIs** | $\to \qquad$ IBGE/SIDRA <br> $\to \qquad$ BCB/SGS |
| **Qualidade** | $\to \qquad$ Black <br> $\to \qquad$ Ruff <br> $\to \qquad$ Pre-commit |  
| **Visualização** | $\to \qquad$ Matplotlib <br> $\to \qquad$ Seaborn |  
| **Infra** | $\to \qquad$ Dockerfile <br> $\to \qquad$ .env |  

<br>

## 🌳 Estrutura do Repositório

```text
.
├── notebooks/
│   ├── 01_selic.ipynb
│   ├── 02_ipca.ipynb
│   ├── 02.01_ipcaAlimentacao.ipynb
│   ├── 03_decomposicao.ipynb
│   ├── 04_analises_avancadas.ipynb
│   ├── 05_ipca_vs_selic.ipynb
│   ├── 06_blocos_macro.ipynb
│   ├── 07_curva_phillips.ipynb
│   ├── 08_modelos_estatisticos.ipynb
│   ├── 09_modelos_ml.ipynb
│   └── 10_dashboard.ipynb
│
├── src/
│   ├── api/
│   │   ├── sidra_client.py
│   │   ├── bcb_client.py
│   │   └── sgs_series.py
│   ├── pipelines/
│   │   ├── ipca.py
│   │   ├── ipca_alimentacao.py
│   │   ├── ipca_habitacao.py
│   │   ├── selic_meta.py
│   │   └── selic_over.py
│   ├── database/
│   │   ├── connection.py
│   │   └── load.py
│   └── utils/
│       ├── logging.py
│       └── cache.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── logs/
│   └── pipeline.log
│
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

<br>

## 🗄 Banco de Dados

| Banco | Tec |
|-|-|
| **Conexão** | $\to \qquad$ `src/database/connection.py` |
| **Criação e inserção** | $\to \qquad$ `src/database/load.py` |
| **Funções:** | $\to \qquad$ ensure_table() <br> $\to \qquad$ insert_all()  

<br>

## 🌐 APIs Integradas

### IBGE/SIDRA  
- Tabelas 1737, 1419, 7060  
- IPCA geral, grupos, subgrupos, itens e subitens  

### BCB/SGS  
- SELIC meta  
- SELIC over  
- Outras séries monetárias  

<br>

## 🔄 Pipelines

| Pipeline | Tec |
|-|-|
| IPCA Geral | $\to \qquad$ `src/pipelines/ipca.py` |
| IPCA – Grupos | $\to \qquad$ `src/pipelines/ipca_grupos.py` |
| IPCA – Sub-Grupos | $\to \qquad$ `src/pipelines/ipca_subgrupos.py` |
| IPCA – Itens | $\to \qquad$ `src/pipelines/ipca_itens.py` |
| IPCA – Sub-Itens | $\to \qquad$ `src/pipelines/ipca_subitens.py` |
| SELIC | $\to \qquad$ `src/pipelines/selic_meta.py` <br> $\to \qquad$ `src/pipelines/selic_over.py` |

<br>

## 📓 Notebooks Educacionais

Cada notebook combina:

- explicação econômica  
- consulta ao banco  
- gráficos profissionais  
- análises interpretáveis  

Exemplos:

- NB3 – Decomposição do IPCA  
- NB4 – Difusão, núcleos, momentum  
- NB5 – IPCA vs SELIC (defasagens, VAR)  
- NB7 – Curva de Phillips  
- NB9 – Machine Learning  

<br>

## 🧹 Qualidade de Código

- Black (formatação)  
- Ruff (linting)  
- Pre-commit (automação)  

Rodar:

```
pre-commit run --all-files
```

<br>

## 🧪 Testes Automatizados

Pasta:

```
tests/
```

Testes garantem:

- integridade dos pipelines  
- importabilidade dos módulos  
- consistência das funções  

Rodar:

```
pytest
```

<br>

## ▶️ Como Executar

| Ação | Execução |
|-|-|
| 1. Criar ambiente | $\to \qquad$ python -m venv .venv <br> $\to \qquad$ source .venv/bin/activate |
| 2. Instalar dependências | $\to \qquad$ pip install -r requirements.txt |
| 3. Configurar .env | $\to \qquad$ cp .env.example .env |
| 4. Rodar pipeline | $\to \qquad$ from src.pipelines.ipca import run_ipca <br> $\to \qquad$ run_ipca() |
| 5. Abrir notebooks | $\to \qquad$ jupyter lab |

<br>

## 🧭 Roadmap

### Próximos passos

- Painel consolidado dos 9 grupos do IPCA  
- Modelos híbridos (VAR + ML)  
- Dashboard em Streamlit  
- Exportação automática de relatórios  
- Monitoramento contínuo (cron + logs)  

<br>

## 🧠 Filosofia

### 1. Rigor técnico  
Pipelines reprodutíveis, logs, testes, banco relacional.

### 2. Transparência  
Notebooks explicativos, gráficos claros, documentação.

### 3. Extensibilidade  
Arquitetura modular, fácil de evoluir.

<br>

## ✔️ Conclusão

Este repositório é uma infraestrutura completa de dados macroeconômicos, combinando engenharia, economia e ciência de dados — ideal para estudos, ensino, pesquisa e aplicações profissionais.
