import pandas as pd
import requests

from src.utils.logging import get_logger

logger = get_logger(__name__)


def sidra_query(
    tabela: int,
    variavel: int,
    periodo: str = "all",
    classificacao: dict | None = None,
):
    logger.info(
        f"Consultando SIDRA: tabela={tabela}, variavel={variavel}, periodo={periodo}"
    )

    # Monta URL base
    url = f"https://apisidra.ibge.gov.br/values/t/{tabela}/n1/all/v/{variavel}/p/{periodo}"

    # Adiciona classificações
    if classificacao:
        for classe, valor in classificacao.items():
            url += f"/c{classe}/{valor}"

    # Força JSON
    url += "?formato=json"
    r = requests.get(url)
    r.raise_for_status()

    data = r.json()

    # Remove metadados
    df = pd.DataFrame(data).iloc[1:].reset_index(drop=True)
    #    logger.info(f"Linhas recebidas (incluindo não válidas): {len(df)}")

    # Renomeia
    df = df.rename(
        columns={
            "D3C": "periodo",
            "D4N": "categoria",
            "V": "valor",
        }
    )

    # Filtra datas válidas
    df = df[df["periodo"].str.match(r"^\d{6}$")]
    #    logger.info(f"Linhas com período válido (AAAAMM): {len(df)}")

    # Converte valores
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    logger.info("Pipeline para conversão de valores concluído com sucesso.")

    return df
