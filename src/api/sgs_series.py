import pandas as pd
import requests
from datetime import datetime, timedelta
from .bcb_client import BCBClient


# Código para acessar séries do SGS (Sistema Gerenciador de Séries Temporais) do Banco Central do Brasil.
def get_bc_series(codigo_serie: int, data_inicial: str, data_final: str) -> pd.DataFrame:
    data = BCBClient.fetch(codigo_serie, data_inicial, data_final)

    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(data)

    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], dayfirst=True)
        df = df.sort_values("data")
    if "valor" in df.columns:
        df["valor"] = df["valor"].str.replace(",", ".").astype(float)

    return df.reset_index(drop=True)


# Obtém a última data válida da série SGS usando o endpoint correto /ultimos/1.
def get_last_valid_date(codigo_serie: int) -> str:
    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados/ultimos/1"
        f"?formato=json"
    )
    response = requests.get(url)

    if not response.text.strip():
        raise RuntimeError("SGS retornou resposta vazia ao consultar a última data.")
    if response.text.strip().startswith("<"):
        raise RuntimeError("SGS retornou HTML ao consultar a última data.")
    data = response.json()
    if not data:
        raise RuntimeError("SGS retornou JSON vazio ao consultar a última data.")
    df = pd.DataFrame(data)
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)

    return df["data"].max().strftime("%d/%m/%Y")


# chamada dos dados em chunks de 10 anos para evitar problemas de timeout ou limites de registros do SGS.
def get_bc_full_series(codigo_serie: int, start: str, end: str) -> pd.DataFrame:
    start_dt = datetime.strptime(start, "%d/%m/%Y")
    end_dt = datetime.strptime(end, "%d/%m/%Y")

    dfs = []
    current_start = start_dt

    while current_start < end_dt:
        current_end = min(current_start + timedelta(days=365*10), end_dt)
        df_chunk = get_bc_series(
            codigo_serie,
            current_start.strftime("%d/%m/%Y"),
            current_end.strftime("%d/%m/%Y")
        )
        dfs.append(df_chunk)
        current_start = current_end + timedelta(days=1)

    df = pd.concat(dfs, ignore_index=True)
    return df.drop_duplicates(subset="data").sort_values("data").reset_index(drop=True)
