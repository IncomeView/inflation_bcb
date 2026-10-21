# PROJECT KNOWLEDGE BASE

Gerado em: 2026-10-20 21:22:10

---

## Estatísticas

- Scripts Python: 41
- Classes: 2
- Funções: 68
- Dependências internas: 48
- Arquivos de configuração: 6

---

## Estrutura do Projeto

```text
inflation

src/
├── api
│   ├── bcb_client.py
│   ├── ipca_series.py
│   ├── sgs_series.py
│   └── sidra_client.py
├── config
│   └── series_config.py
├── core
│   ├── __init__.py
│   ├── cache.py
│   ├── logging.py
│   └── validate.py
├── database
│   ├── migrations
│   │   ├── 001_create_tables.sql
│   │   ├── 002_create_views.sql
│   │   └── 003_alter_tables.sql
│   ├── __init__.py
│   ├── connection.py
│   └── load.py
├── domain
│   ├── inflation
│   ├── ipca
│   │   └── taxonomia.py
│   ├── selic
│   └── __init__.py
├── pipelines
│   ├── ipca
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── geral.py
│   │   ├── grupos.py
│   │   ├── itens.py
│   │   ├── subgrupos.py
│   │   ├── subitens.py
│   │   └── taxonomia.py
│   ├── __init__.py
│   ├── run_all.py
│   ├── selic_meta.py
│   └── selic_over.py
├── services
│   ├── __init__.py
│   ├── audit.py
│   └── health_check.py
├── utils
│   └── dtypes.py
└── main.py

tests/
├── data_quality
│   ├── test_database_quality.py
│   ├── test_ipca_taxonomia.py
│   ├── test_series_config.py
│   └── test_validation.py
├── test_api_structure.py
├── test_config.py
├── test_imports.py
├── test_pipelines_structure.py
├── test_taxonomia.py
└── test_utils.py

docs/
├── architecture.md
├── business_rules.md
├── data_dictionary.md
├── pipeline.md
└── runbook.md

```

---

## Arquivos de Configuração

- pyproject.toml
- requirements.txt
- Dockerfile
- docker-compose.yml
- Makefile
- README.md

---

## Visão Arquitetural

### APIs

- src/api/bcb_client.py
- src/api/sidra_client.py
- src/api/sgs_series.py


---

## Fluxo de Dados

## Mapa de Dependências

### src/api/bcb_client.py

- src.core.logging

### src/api/ipca_series.py

- src.api.sidra_client

### src/api/sgs_series.py

- src.api.bcb_client
- src.config.series_config
- src.core.logging

### src/api/sidra_client.py

- src.core.logging

### src/database/load.py

- src.core.validate
- src.database.connection

### src/main.py

- src.pipelines.selic_meta
- src.pipelines.selic_over

### src/pipelines/ipca/base.py

- src.api.sidra_client

### src/pipelines/ipca/geral.py

- src.api.sidra_client
- src.database.load

### src/pipelines/ipca/grupos.py

- src.database.load
- src.pipelines.ipca.base

### src/pipelines/ipca/itens.py

- src.database.load
- src.pipelines.ipca.base

### src/pipelines/ipca/subgrupos.py

- src.database.load
- src.pipelines.ipca.base

### src/pipelines/ipca/subitens.py

- src.database.load
- src.pipelines.ipca.base

### src/pipelines/ipca/taxonomia.py

- src.database.connection
- src.database.load
- src.domain.ipca.taxonomia

### src/pipelines/run_all.py

- src.pipelines.ipca.geral
- src.pipelines.ipca.grupos
- src.pipelines.ipca.itens
- src.pipelines.ipca.subgrupos
- src.pipelines.ipca.subitens
- src.pipelines.ipca.taxonomia
- src.pipelines.selic_meta
- src.pipelines.selic_over

### src/pipelines/selic_meta.py

- src.api.sgs_series
- src.database.load

### src/pipelines/selic_over.py

- src.api.sgs_series
- src.database.load

### src/services/audit.py

- src.services.health_check

### src/services/health_check.py

- src.database.connection

### tests/data_quality/test_database_quality.py

- src.database.connection

### tests/data_quality/test_ipca_taxonomia.py

- src.domain.ipca.taxonomia

### tests/data_quality/test_series_config.py

- src.config.series_config

### tests/data_quality/test_validation.py

- src.core.validate

### tests/test_api_structure.py

- src.api.bcb_client

### tests/test_config.py

- src.config.series_config

### tests/test_pipelines_structure.py

- src.pipelines.selic_meta
- src.pipelines.selic_over

### tests/test_taxonomia.py

- src.domain.ipca.taxonomia

### tests/test_utils.py

- src.core.cache

---

## Documentação Funcional

### architecture.md

```markdown
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
```

### business_rules.md

```markdown

```

### data_dictionary.md

```markdown
> data_dictionary.md

# bcb.ipca_geral

Fonte:
SIDRA 1737

Grão:
1 linha por mês

Atualização:
Mensal

Campos:

date
indice
acumulado
acumulado12m
nindice


# bcb.ipca_subitens

Fonte:
SIDRA 7060

Grão:
1 linha por mês e subitem


# bcb.ipca_taxonomia

Classificação proprietária do projeto.

Responsável:
domain/ipca/taxonomia.py
```

### pipeline.md

```markdown
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
```

### runbook.md

```markdown
# Runbook

## Atualizar dados

python -m src.main

## Executar testes

pytest

## Auditoria

python -m src.services.audit

## Gerar relatórios

quarto render
```

---

## Catálogo de Scripts

# src/api/bcb_client.py

## Imports

- requests
- src.core.logging
- time
- typing

## Classes

### BCBClient

## Funções

### _build_url()

### fetch()

### get_series()

---

# src/api/ipca_series.py

## Imports

- pandas
- src.api.sidra_client

## Funções

### get_ipca_grupo()

Retorna a série histórica de um grupo do IPCA.
Tabela 1419, variável 63 (variação mensal).
Classificação 315 = grupos do IPCA.

### get_ipca_geral()

Retorna a série histórica completa do IPCA geral (SIDRA 1737).

Variáveis:
    63    = variação mensal        -> indice
    2266  = número-índice          -> nindice
    69    = acumulado no ano       -> acumulado
    2265  = acumulado em 12 meses  -> acumulado12m

---

# src/api/sgs_series.py

## Imports

- datetime
- pandas
- requests
- src.api.bcb_client
- src.config.series_config
- src.core.logging

## Funções

### get_series()

Obtém a série completa do BCB/SGS usando:
- primeira data configurada (series_config)
- última data válida (SGS)

### get_bc_series()

### get_last_valid_date()

### get_bc_full_series()

---

# src/api/sidra_client.py

## Imports

- pandas
- requests
- src.core.logging

## Funções

### sidra_query()

---

# src/config/series_config.py

## Funções

### get_first_date()

---

# src/core/__init__.py

---

# src/core/cache.py

## Classes

### Cache

## Funções

### __init__()

### get()

### set()

### clear()

---

# src/core/logging.py

## Imports

- logging
- pathlib

## Funções

### get_logger()

---

# src/core/validate.py

## Funções

### validate_df()

---

# src/database/__init__.py

---

# src/database/connection.py

## Imports

- dotenv
- os
- sqlalchemy

---

# src/database/load.py

## Imports

- pandas
- sqlalchemy
- src.core.validate
- src.database.connection

## Funções

### safe_replace()

### insert_all()

### truncate_table()

---

# src/domain/__init__.py

---

# src/domain/ipca/taxonomia.py

## Funções

### get_taxonomia()

### get_bloco_macro()

### get_categoria_cidada()

---

# src/main.py

## Imports

- src.pipelines.selic_meta
- src.pipelines.selic_over

## Funções

### main()

---

# src/pipelines/__init__.py

---

# src/pipelines/ipca/__init__.py

---

# src/pipelines/ipca/base.py

## Imports

- pandas
- src.api.sidra_client

## Funções

### get_ipca_nivel()

---

# src/pipelines/ipca/geral.py

## Imports

- pandas
- src.api.sidra_client
- src.database.load

## Funções

### get_ipca_geral()

### run_ipca_geral()

### main()

---

# src/pipelines/ipca/grupos.py

## Imports

- src.database.load
- src.pipelines.ipca.base

## Funções

### run_ipca_grupos()

### main()

---

# src/pipelines/ipca/itens.py

## Imports

- src.database.load
- src.pipelines.ipca.base

## Funções

### run_ipca_itens()

### main()

---

# src/pipelines/ipca/subgrupos.py

## Imports

- src.database.load
- src.pipelines.ipca.base

## Funções

### run_ipca_subgrupos()

### main()

---

# src/pipelines/ipca/subitens.py

## Imports

- src.database.load
- src.pipelines.ipca.base

## Funções

### run_ipca_subitens()

### main()

---

# src/pipelines/ipca/taxonomia.py

## Imports

- pandas
- src.database.connection
- src.database.load
- src.domain.ipca.taxonomia

## Funções

### build_taxonomia()

### validate_taxonomia()

### run_taxonomia()

### main()

---

# src/pipelines/run_all.py

## Imports

- src.pipelines.ipca.geral
- src.pipelines.ipca.grupos
- src.pipelines.ipca.itens
- src.pipelines.ipca.subgrupos
- src.pipelines.ipca.subitens
- src.pipelines.ipca.taxonomia
- src.pipelines.selic_meta
- src.pipelines.selic_over

## Funções

### run_all()

### main()

---

# src/pipelines/selic_meta.py

## Imports

- src.api.sgs_series
- src.database.load

## Funções

### run_selic_meta()

### main()

---

# src/pipelines/selic_over.py

## Imports

- src.api.sgs_series
- src.database.load

## Funções

### run_selic_over()

### main()

---

# src/services/__init__.py

---

# src/services/audit.py

## Imports

- pprint
- src.services.health_check

## Funções

### main()

---

# src/services/health_check.py

## Imports

- pandas
- src.database.connection

## Funções

### validate_database()

---

# src/utils/dtypes.py

## Funções

### apply_dtypes()

---

# tests/data_quality/test_database_quality.py

## Imports

- pandas
- src.database.connection

## Funções

### test_ipca_geral_not_empty()

### test_ipca_sem_data_futura()

### test_ipca_subitens_sem_duplicatas()

### test_taxonomia_sem_nulos()

---

# tests/data_quality/test_ipca_taxonomia.py

## Imports

- src.domain.ipca.taxonomia

## Funções

### test_taxonomia_tem_subgrupos()

---

# tests/data_quality/test_series_config.py

## Imports

- src.config.series_config

## Funções

### test_series_codes()

---

# tests/data_quality/test_validation.py

## Imports

- pandas
- src.core.validate

## Funções

### test_empty_dataframe()

### test_missing_columns()

### test_valid_dataframe()

---

# tests/test_api_structure.py

## Imports

- src.api.bcb_client

## Funções

### test_bcb_client_has_get_method()

### test_bcb_client_init()

---

# tests/test_config.py

## Imports

- src.config.series_config

## Funções

### test_series_config_structure()

### test_series_config_items()

---

# tests/test_imports.py

## Funções

### test_import_main_modules()

---

# tests/test_pipelines_structure.py

## Imports

- src.pipelines.selic_meta
- src.pipelines.selic_over

## Funções

### test_selic_over_has_main()

### test_selic_meta_has_main()

---

# tests/test_taxonomia.py

## Imports

- src.domain.ipca.taxonomia

## Funções

### test_subitem_taxonomia()

---

# tests/test_utils.py

## Imports

- src.core.cache

## Funções

### test_cache_initialization()

### test_cache_has_default_path()

---

