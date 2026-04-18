SGS - Sistema gerador de séries temporais

# 📘 Plano do Projeto — Impacto da Inflação no Poder de Compra do Brasileiro

Este projeto tem como objetivo analisar, modelar e visualizar **como a inflação afeta o poder de compra real dos trabalhadores brasileiros**, utilizando dados oficiais, estatística aplicada e técnicas de machine learning.

O foco principal é transformar dados econômicos complexos em **informações claras, acessíveis e úteis**, respondendo perguntas como:

- Quanto o salário real caiu ao longo dos anos  
- Quais grupos de consumo mais pressionam o orçamento  
- Como a inflação afeta diferentes faixas de renda  
- Qual é o custo de vida real nas regiões do Brasil  
- Como o poder de compra evolui em cenários futuros  

---

# 🧭 Visão Geral do Projeto

O projeto está dividido em fases, cada uma com entregáveis claros e independentes.

---

# **Fase 1 — Ambiente e Infraestrutura (Concluída)**

- Estrutura de pastas organizada  
- Ambiente virtual configurado  
- Dependências controladas (`requirements.txt`)  
- Repositório Git configurado  
- Workflow CI/CD com GitHub Actions  
- Execução automática de todos os pipelines em `src/pipelines/`  
- Versionamento por TAG (ex: `v0.1.1`)  
- Artifacts para resultados (raw, processed, outputs)  
- Cache de dependências  

**Objetivo:** garantir uma base sólida, reprodutível e profissional para o projeto.

---

# **Fase 2 — Coleta e Engenharia de Dados (Em andamento)**

Nesta fase, coletaremos e estruturaremos todos os dados necessários para medir o poder de compra real.

### 📌 Inflação  
- IPCA geral  
- IPCA por grupo (alimentação, transporte, habitação etc.)  
- IPCA por subitem  
- INPC (inflação para famílias de baixa renda)  
- IPCA por região  

### 📌 Renda  
- Salário mínimo histórico (IBGE)  
- Rendimento médio real do trabalhador (PNAD Contínua)  
- Renda por setor e região  

### 📌 Custo de vida  
- Cesta básica (DIEESE)  
- Aluguel (FIPE/ZAP)  
- Gasolina (ANP)  
- Energia elétrica (ANEEL)  

### 📌 Metadados  
- Datas de coleta  
- Versão do pipeline  
- Fonte dos dados  
- Transformações aplicadas  
- Tamanho e formato dos arquivos  

**Objetivo:** montar uma base de dados completa, limpa e padronizada.

---

# **Fase 3 — Estatística Aplicada**

Com os dados estruturados, iniciaremos análises estatísticas para medir o impacto real da inflação no bolso do brasileiro.

### Exemplos de análises:

- Evolução do salário real  
- Perda acumulada do poder de compra  
- Comparação entre inflação geral e inflação de alimentos  
- Impacto da inflação por faixa de renda  
- Custo da cesta básica vs salário mínimo  
- Diferenças regionais no custo de vida  

**Objetivo:** quantificar o impacto da inflação de forma clara e objetiva.

---

# **Fase 4 — Machine Learning**

Aplicaremos modelos para prever tendências e simular cenários futuros.

### Possíveis modelos:

- Regressão para prever inflação por grupo  
- Modelos para estimar salário real futuro  
- Modelos para simular impacto de choques (ex: gasolina +20%)  
- Modelos para estimar custo de vida por região  

**Objetivo:** criar previsões e simulações úteis para tomada de decisão.

---

# **Fase 5 — Visualização e Comunicação**

Criação de gráficos, dashboards e relatórios para comunicar os resultados.

### Entregáveis:

- Gráficos de evolução do poder de compra  
- Comparações entre regiões e faixas de renda  
- Painéis interativos (futuro)  
- Relatórios automatizados  

**Objetivo:** tornar os resultados acessíveis e visualmente claros.

---

# **Status Atual**

- Ambiente configurado  
- CI/CD funcionando  
- Pipelines iniciais (SELIC) rodando  
- Versionamento por TAG ativo  
- Preparação para coleta de dados do IPCA e renda  

---

# **Próximos Passos**

1. Implementar pipeline do IPCA  
2. Implementar pipeline de salário mínimo  
3. Implementar pipeline de rendimento médio (PNAD)  
4. Criar pipeline de metadados  
5. Integrar dados em uma base unificada  
6. Iniciar análises estatísticas  

