import pandas as pd

from src.api.sidra_client import sidra_query
from src.database.load import ensure_table, insert_all

SUBGRUPOS_HABITACAO = {
    "7178": "habitacao",
    "7179": "aluguel_e_taxas",
    "7180": "condominio",
    "7181": "energia_eletrica_residencial",
    "7182": "agua_e_esgoto",
    "7183": "gas_encanado",
    "7184": "artigos_de_limpeza",
    "7185": "servicos_de_manutencao_do_lar",
}


def run_ipca_habitacao():

    df = sidra_query(
        tabela=1419,
        variavel=63,
        periodo="all",
        classificacao={"315": ",".join(SUBGRUPOS_HABITACAO.keys())},
    )

    # Mantém apenas os subgrupos desejados
    df = df[df["D4C"].isin(SUBGRUPOS_HABITACAO.keys())]
    #   logger.info(f"Linhas após filtrar subgrupos: {len(df)}")

    # Normaliza colunas
    df = df.rename(
        columns={
            "periodo": "date",
            "valor": "value",
            "D4C": "codigo",
        }
    )

    df["date"] = pd.to_datetime(df["date"], format="%Y%m")

    # Pivot
    df = df.pivot_table(index="date", columns="codigo", values="value").reset_index()

    # Renomeia colunas
    df = df.rename(columns=SUBGRUPOS_HABITACAO)

    # Garante que TODAS as colunas existam
    for col in SUBGRUPOS_HABITACAO.values():
        if col not in df.columns:
            df[col] = None

    # Ordena colunas
    df = df[["date"] + list(SUBGRUPOS_HABITACAO.values())]

    # Cria tabela e insere
    table = "ipca_habitacao"
    ensure_table(df, table, schema="bcb")
    insert_all(df, table, schema="bcb")
