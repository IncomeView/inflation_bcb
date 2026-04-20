import pandas as pd

from src.api.sidra_client import sidra_query
from src.database.load import ensure_table, insert_all

SUBGRUPOS = {
    "7169": "alimentacao_e_bebidas",
    "7170": "alimentacao_no_domicilio",
    "7171": "alimentacao_fora_do_domicilio",
    "7172": "cereais_leguminosas_oleaginosas",
    "7173": "carnes",
    "7174": "leite_e_derivados",
    "7175": "frutas",
    "7176": "tuberculos_raizes_legumes",
    "7177": "panificados",
}


def run_ipca_alimentacao():

    df = sidra_query(
        tabela=1419,
        variavel=63,
        periodo="all",
        classificacao={"315": "7169,7170,7171,7172,7173,7174,7175,7176,7177"},
    )

    # Mantém apenas os subgrupos desejados
    df = df[df["D4C"].isin(SUBGRUPOS.keys())]

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
    df = df.rename(columns=SUBGRUPOS)

    # Garante que TODAS as colunas existam
    for col in SUBGRUPOS.values():
        if col not in df.columns:
            df[col] = None  # ou pd.NA

    # Ordena colunas
    df = df[["date"] + list(SUBGRUPOS.values())]

    # Cria tabela e insere
    table = "ipca_alimentacao"
    ensure_table(df, table, schema="bcb")
    insert_all(df, table, schema="bcb")

    return True
