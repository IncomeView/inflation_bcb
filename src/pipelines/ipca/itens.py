# src/pipelines/ipca/itens.py

import pandas as pd

from src.api.sidra_client import sidra_query
from src.database.load import insert_all, truncate_table


def get_ipca_itens(periodo="all"):
    df_valor = sidra_query(
        tabela=7060,
        variavel=63,
        periodo=periodo,
        classificacao={"327": "all"},
    ).rename(columns={"valor": "indice"})

    df_peso = sidra_query(
        tabela=7060,
        variavel=66,
        periodo=periodo,
        classificacao={"327": "all"},
    ).rename(columns={"valor": "peso"})

    df = df_valor.merge(
        df_peso[["periodo", "categoria", "peso"]],
        on=["periodo", "categoria"],
        how="left",
    )

    df["category"] = df["categoria"].apply(lambda x: str(x).split(".")[0])
    df["category_name"] = df["categoria"].apply(
        lambda x: str(x).split(".")[1] if "." in str(x) else None
    )

    df = df.rename(columns={"periodo": "date"})
    df["date"] = pd.to_datetime(df["date"], format="%Y%m")

    return df[["date", "indice", "peso", "category", "category_name"]]


def run_ipca_itens(periodo="all"):
    df = get_ipca_itens(periodo)

    truncate_table("ipca_itens", schema="bcb")
    insert_all(df, "ipca_itens", schema="bcb")

    print("Tabela bcb.ipca_itens atualizada com sucesso!")


if __name__ == "__main__":
    run_ipca_itens()
