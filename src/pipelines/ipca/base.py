import pandas as pd

from src.api.sidra_client import sidra_query
from src.pipelines.ipca.codigos import codigos


def get_ipca_nivel(nivel_codes, periodo="all"):
    # Variação mensal
    df_indice = sidra_query(
        tabela=7060,
        variavel=63,
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "indice"})

    # Peso
    df_peso = sidra_query(
        tabela=7060,
        variavel=66,
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "peso"})

    # Acumulado no ano
    df_acum = sidra_query(
        tabela=7060,
        variavel=2265,
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "acumulado"})

    # MERGE das variáveis
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

    # Filtra pelos códigos internos (D4C)
    df = df[df["categoria"].isin(nivel_codes)]

    # Merge para trazer o nome da categoria (D4N)
    df = df.merge(codigos, left_on="categoria", right_on="D4C", how="left")

    # Separar category e category_name
    df["category"] = df["D4N"].apply(lambda x: str(x).split(".")[0])
    df["category_name"] = df["D4N"].apply(
        lambda x: str(x).split(".", 1)[1] if "." in str(x) else x
    )

    # Ajustar data
    df = df.rename(columns={"periodo": "date"})
    df["date"] = pd.to_datetime(df["date"], format="%Y%m")

    return df[["date", "indice", "acumulado", "peso", "category", "category_name"]]
