from datetime import datetime, timedelta

import pandas as pd
import requests

from src.api.bcb_client import BCBClient
from src.utils.logging import get_logger

logger = get_logger(__name__)


def get_bc_series(codigo_serie: int, data_inicial: str, data_final: str) -> pd.DataFrame:
    data = BCBClient.fetch(codigo_serie, data_inicial, data_final)

    if not data:
        logger.warning(
            f"Nenhum dado retornado pelo SGS para o período "
            f"{data_inicial} → {data_final}"
        )
        return pd.DataFrame()

    df = pd.DataFrame(data)

    # Conversão da coluna de data
    if "data" in df.columns:
        try:
            df["data"] = pd.to_datetime(df["data"], dayfirst=True)
            df = df.sort_values("data")
        except Exception as e:
            logger.error(f"Erro ao converter datas para datetime: {e}", exc_info=True)
            raise

    # Conversão da coluna valor
    if "valor" in df.columns:
        try:
            df["valor"] = df["valor"].str.replace(",", ".").astype(float)
        except Exception as e:
            logger.error(f"Erro ao converter valores para float: {e}", exc_info=True)
            raise

    logger.info(
        f"Chunk processado com sucesso | Registros: {len(df)} | "
        f"{data_inicial} → {data_final}"
    )

    return df.reset_index(drop=True)


def get_last_valid_date(codigo_serie: int) -> str:
    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados/ultimos/1"
        f"?formato=json"
    )

    response = requests.get(url)
    text = response.text.strip()

    if not text:
        msg = "SGS retornou resposta vazia ao consultar a última data."
        logger.error(msg)
        raise RuntimeError(msg)

    if text.startswith("<"):
        msg = "SGS retornou HTML ao consultar a última data."
        logger.error(msg)
        raise RuntimeError(msg)

    data = response.json()

    if not data:
        msg = "SGS retornou JSON vazio ao consultar a última data."
        logger.error(msg)
        raise RuntimeError(msg)

    df = pd.DataFrame(data)
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)

    last_date = df["data"].max().strftime("%d/%m/%Y")

    return last_date


def get_bc_full_series(codigo_serie: int, start: str, end: str) -> pd.DataFrame:
    logger.info(
        f"Iniciando coleta completa da série {codigo_serie} | "
        f"Período total: {start} → {end}"
    )

    start_dt = datetime.strptime(start, "%d/%m/%Y")
    end_dt = datetime.strptime(end, "%d/%m/%Y")

    dfs = []
    current_start = start_dt

    while current_start < end_dt:
        current_end = min(current_start + timedelta(days=365 * 10), end_dt)

        df_chunk = get_bc_series(
            codigo_serie,
            current_start.strftime("%d/%m/%Y"),
            current_end.strftime("%d/%m/%Y"),
        )

        dfs.append(df_chunk)
        current_start = current_end + timedelta(days=1)

    df = pd.concat(dfs, ignore_index=True)
    df = df.drop_duplicates(subset="data").sort_values("data").reset_index(drop=True)

    logger.info(
        f"Coleta completa finalizada | Total de registros: {len(df)} | "
        f"Série: {codigo_serie}"
    )

    return df
