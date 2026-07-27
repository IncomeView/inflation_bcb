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
        f"Consultando SIDRA: tabela={tabela} | → variavel={variavel} | periodo={periodo}"
    )

    url = f"https://apisidra.ibge.gov.br/values/t/{tabela}/n1/all/v/{variavel}/p/{periodo}"

    if classificacao:
        for classe, valor in classificacao.items():
            url += f"/c{classe}/{valor}"

    url += "?formato=json"
    r = requests.get(url)
    r.raise_for_status()

    data = r.json()

    df = pd.DataFrame(data).iloc[1:].reset_index(drop=True)

    # RENOMEAÇÃO CORRETA
    df = df.rename(
        columns={
            "D3C": "periodo",  # período AAAAMM
            "D4C": "categoria",  # código da categoria
            "D4N": "categoria_nome",  # nome da categoria
            "V": "valor",  # valor da variável
        }
    )

    # Filtrar datas válidas
    df = df[df["periodo"].str.match(r"^\d{6}$")]

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    logger.info("Pipeline para conversão de valores concluído com sucesso.")

    return df
