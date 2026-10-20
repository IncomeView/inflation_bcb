# codigos.py

import pandas as pd
import requests

url = (
    "https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63/p/all/c315/all?formato=json"
)
r = requests.get(url)
data = r.json()

df = pd.DataFrame(data[1:])  # pula o cabeçalho

# 🔥 Correção definitiva
df["D4C"] = pd.to_numeric(df["D4C"], errors="coerce").astype("Int64")

# Remover linhas onde D4C virou NaN
df = df.dropna(subset=["D4C"])

df["D4C"] = df["D4C"].astype(int)

codigos = df[["D4C", "D4N"]].drop_duplicates().sort_values("D4C")

cod_geral = [7169]
cod_grupos = codigos[codigos["D4C"].between(7170, 7199)]["D4C"].tolist()
cod_subgrupos = codigos[codigos["D4C"].between(7171, 7299)]["D4C"].tolist()
cod_itens = codigos[codigos["D4C"].between(7172, 7399)]["D4C"].tolist()
cod_subitens = codigos[codigos["D4C"].between(7173, 7499)]["D4C"].tolist()
cod_detalhados = codigos[codigos["D4C"] >= 100000]["D4C"].tolist()
