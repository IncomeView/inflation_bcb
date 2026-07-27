import pandas as pd

from src.api.sidra_client import sidra_query


def get_ipca_nivel(prefix_len, periodo="all"):

    df_indice = sidra_query(
        tabela=7060,
        variavel=63,
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "indice"})

    df_peso = sidra_query(
        tabela=7060,
        variavel=66,
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "peso"})

    df_acum = sidra_query(
        tabela=7060,
        variavel=2265,
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "acumulado"})

    df = df_indice.merge(
        df_peso[["periodo", "categoria", "peso"]],
        on=["periodo", "categoria"],
        how="left",
    )

    df = df.merge(
        df_acum[["periodo", "categoria", "acumulado"]],
        on=["periodo", "categoria"],
        how="left",
    )

    # remover linhas sem categoria_nome
    df = df.dropna(subset=["categoria_nome"])

    # dividir categoria_nome corretamente
    split_cols = df["categoria_nome"].str.split(".", n=1, expand=True)
    df["categoria"] = split_cols[0]
    df["categoria_nome"] = split_cols[1]

    df["prefix_len"] = df["categoria"].str.len()

    df = df[df["prefix_len"] == prefix_len]

    df = df.rename(columns={"periodo": "date"})
    df["date"] = pd.to_datetime(df["date"], format="%Y%m")

    return df[["date", "indice", "acumulado", "peso", "categoria", "categoria_nome"]]
