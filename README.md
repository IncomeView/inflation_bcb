# 📈 Inflation Analytics – Brasil  
### IPCA, SELIC, BCB, IBGE/SIDRA • Pipelines Reprodutíveis • PostgreSQL • Notebooks Educacionais

Este projeto reúne **engenharia de dados**, **macroeconomia aplicada** e **educação analítica**.  
Ele foi construído para:

- coletar dados oficiais do **IBGE/SIDRA** e **Banco Central do Brasil (BCB)**  
- organizar séries históricas em **PostgreSQL**  
- criar **pipelines reprodutíveis**  
- gerar **notebooks explicativos** sobre inflação e juros  
- servir como base para modelos, dashboards e estudos econômicos

O objetivo é ter uma infraestrutura sólida, transparente e extensível para análise macroeconômica no Brasil.

---

# 🧭 Sumário

1. [Visão Geral](#visão-geral)  
2. [Arquitetura do Projeto](#arquitetura-do-projeto)  
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
4. [Estrutura do Repositório](#estrutura-do-repositório)  
5. [Banco de Dados – PostgreSQL](#banco-de-dados--postgresql)  
6. [APIs Integradas (BCB e IBGE/SIDRA)](#apis-integradas-bcb-e-ibgesidra)  
7. [Pipelines Implementados](#pipelines-implementados)  
8. [Notebooks Educacionais](#notebooks-educacionais)  
9. [Qualidade de Código (Black, Ruff, Pre-commit)](#qualidade-de-código-black-ruff-pre-commit)  
10. [Testes Automatizados](#testes-automatizados)  
11. [Como Executar o Projeto](#como-executar-o-projeto)  
12. [Roadmap](#roadmap)  
13. [Filosofia do Projeto](#filosofia-do-projeto)

---

# 📌 Visão Geral

Este projeto coleta, transforma e armazena dados econômicos brasileiros, com foco em:

- **IPCA** (grupos, subgrupos, itens)  
- **SELIC** (meta e over)  
- **Séries temporais do BCB**  
- **Estruturação de dados para análises avançadas**

Ele combina:

- engenharia de dados  
- boas práticas de software  
- documentação educacional  
- análises econômicas visuais  

---

# 🏗 Arquitetura do Projeto  

Fluxo geral:

~~~
IBGE/SIDRA → sidra_query() → pipelines IPCA → PostgreSQL → notebooks
BCB/SGS   → bcb_client()  → pipelines SELIC → PostgreSQL → notebooks
~~~

Componentes principais:

- **API Clients**: abstrações para BCB e IBGE  
- **Pipelines ETL**: scripts reprodutíveis para cada grupo do IPCA e para SELIC  
- **PostgreSQL**: armazenamento estruturado  
- **Logging**: rastreamento profissional  
- **Notebooks**: explicações econômicas + visualizações  
- **Testes**: garantem integridade estrutural  
- **Ferramentas de qualidade**: Black, Ruff, pre-commit  

---

# 🛠 Tecnologias Utilizadas

### Linguagem
- Python 3.12

### Banco de Dados
- PostgreSQL + SQLAlchemy

### APIs
- **IBGE/SIDRA** (tabela 1419 – IPCA)  
- **BCB/SGS** (SELIC e outras séries)

### Ferramentas de Qualidade
- **Black** (formatação)  
- **Ruff** (linting)  
- **pre-commit** (hooks automáticos)

### Visualização
- Matplotlib  
- Seaborn  

### Infra
- Dockerfile (opcional)  
- `.env` para credenciais  

---

# 🌳 Estrutura do Repositório

Trecho relevante da árvore (resumido):

~~~
.
├── notebooks/
│   ├── 01_selic.ipynb
│   ├── 02.01_ipcaAlimentacao.ipynb
│   ├── 02_ipca.ipynb
│   └── model.ipynb
├── src/
│   ├── api/
│   │   ├── sidra_client.py
│   │   ├── bcb_client.py
│   │   └── sgs_series.py
│   ├── pipelines/
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
├── logs/pipeline.log
├── requirements.txt
├── pyproject.toml
└── README.md
~~~

---

# 🗄 Banco de Dados – PostgreSQL

O projeto usa PostgreSQL como backend principal.

### Conexão

Arquivo:

~~~
src/database/connection.py
~~~

Cria engine SQLAlchemy a partir de variáveis `.env`.

### Criação e inserção de tabelas

Arquivo:

~~~
src/database/load.py
~~~

Funções:

- `ensure_table(df, table, schema="bcb")`  
- `insert_all(df, table, schema="bcb")`

### Observação importante

Quando o schema muda (ex: pivot wide), é necessário dropar a tabela:

~~~
DROP TABLE bcb.ipca_alimentacao;
~~~

---

# 🌐 APIs Integradas (BCB e IBGE/SIDRA)

## IBGE/SIDRA – IPCA

Cliente robusto:

~~~
src/api/sidra_client.py
~~~

Principais pontos:

- monta URL da API  
- aceita classificações (ex: 315 – grupos do IPCA)  
- converte `"..."` → NaN  
- filtra períodos válidos (AAAAMM)  
- retorna DataFrame limpo  

## BCB – SGS

Clientes:

- `bcb_client.py`  
- `sgs_series.py`  

Usados para:

- SELIC meta  
- SELIC over  
- outras séries do SGS  

---

# 🔄 Pipelines Implementados

## 1. IPCA – Alimentação e Bebidas

Arquivo:

~~~
src/pipelines/ipca_alimentacao.py
~~~

Subgrupos:

~~~
7169 → alimentacao_e_bebidas
7170 → alimentacao_no_domicilio
7171 → alimentacao_fora_do_domicilio
7172 → cereais_leguminosas_oleaginosas
7173 → carnes
7174 → leite_e_derivados
7175 → frutas
7176 → tuberculos_raizes_legumes
7177 → panificados
~~~

Processo:

- consulta SIDRA  
- filtra subgrupos  
- renomeia colunas  
- pivot wide  
- garante colunas faltantes  
- grava em `bcb.ipca_alimentacao`  

---

## 2. IPCA – Habitação

Arquivo:

~~~
src/pipelines/ipca_habitacao.py
~~~

Subgrupos:

~~~
7178 → habitacao
7179 → aluguel_e_taxas
7180 → condominio
7181 → energia_eletrica_residencial
7182 → agua_e_esgoto
7183 → gas_encanado
7184 → artigos_de_limpeza
7185 → servicos_de_manutencao_do_lar
~~~

Mesma estrutura do pipeline anterior.

---

## 3. SELIC – Meta e Over

Arquivos:

~~~
src/pipelines/selic_meta.py
src/pipelines/selic_over.py
~~~

Usam SGS/BCB para:

- baixar séries  
- limpar  
- padronizar  
- gravar em PostgreSQL  

---

# 📓 Notebooks Educacionais

Os notebooks seguem um padrão **prático + educacional**:

- introdução conceitual  
- explicação dos grupos/subgrupos  
- execução do pipeline  
- consulta ao banco  
- gráficos profissionais  
- conclusões econômicas  

Exemplos:

### `02.01_ipcaAlimentacao.ipynb`

Contém:

- explicação do grupo Alimentação  
- subgrupos oficiais  
- execução do pipeline  
- heatmap  
- média móvel  
- conclusões  

### Notebook de Habitação

Segue exatamente o mesmo modelo.

---

# 🧹 Qualidade de Código – Black, Ruff, Pre-commit

Configurações em:

~~~
pyproject.toml
.pre-commit-config.yaml
~~~

### Black

- formatação automática  
- estilo consistente  

### Ruff

- linting rápido  
- substitui flake8 + isort  

### Pre-commit

Instalação:

~~~
pre-commit install
~~~

Rodar manualmente:

~~~
pre-commit run --all-files
~~~

---

# 🧪 Testes Automatizados

Pasta:

~~~
tests/
~~~

Testes garantem:

- estrutura dos módulos  
- importabilidade  
- presença de funções essenciais  
- integridade dos pipelines  
- funcionamento dos utilitários  

Rodar:

~~~
pytest
~~~

---

# ▶️ Como Executar o Projeto

## 1. Criar ambiente virtual

~~~
python -m venv .venv
source .venv/bin/activate
~~~

## 2. Instalar dependências

~~~
pip install -r requirements.txt
~~~

## 3. Configurar `.env`

Copiar:

~~~
cp .env.example .env
~~~

Preencher:

- POSTGRES_HOST  
- POSTGRES_USER  
- POSTGRES_PASSWORD  
- POSTGRES_DB  

## 4. Rodar um pipeline

~~~
from src.pipelines.ipca_alimentacao import run_ipca_alimentacao
run_ipca_alimentacao()
~~~

## 5. Abrir notebooks

~~~
jupyter lab
~~~

---

# 🧭 Roadmap

### Próximos grupos do IPCA

- Transportes  
- Saúde e cuidados pessoais  
- Educação  
- Comunicação  
- Vestuário  
- Artigos de residência  
- Despesas pessoais  

### Projetos futuros

- reconstrução do IPCA geral  
- painel consolidado dos 9 grupos  
- modelos de previsão (ARIMA, VAR, ETS)  
- decomposição de choques  
- dashboards (Streamlit / Power BI)  

---

# 🧠 Filosofia do Projeto

Este projeto foi construído com três pilares:

## 1. **Rigor técnico**
- pipelines reprodutíveis  
- logs profissionais  
- banco relacional  
- testes automatizados  
- linting e formatação  

## 2. **Transparência e educação**
- notebooks explicativos  
- gráficos claros  
- narrativa econômica  
- documentação detalhada  

## 3. **Extensibilidade**
- qualquer grupo do IPCA pode ser adicionado  
- qualquer série do BCB pode ser integrada  
- arquitetura modular  
- fácil de evoluir para modelos e dashboards  

---

# ✔️ Conclusão

Este repositório é mais que um conjunto de scripts:  
é uma **infraestrutura completa de dados macroeconômicos**,  
combinando engenharia, economia e educação.

