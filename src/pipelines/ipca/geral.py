# src/pipelines/ipca/geral.py

import pandas as pd

from src.api.sidra_client import sidra_query
from src.database.load import safe_replace


def get_ipca_geral(periodo="all"):

    # Número-índice (2266)
    df_nindice = sidra_query(
        tabela=1737,
        variavel=2266,
        periodo=periodo,
    )[
        ["periodo", "valor"]
    ].rename(columns={"valor": "nindice"})

    # Variação mensal (63)
    df_indice = sidra_query(
        tabela=1737,
        variavel=63,
        periodo=periodo,
    )[
        ["periodo", "valor"]
    ].rename(columns={"valor": "indice"})

    # Acumulado no ano (69)
    df_acum = sidra_query(
        tabela=1737,
        variavel=69,
        periodo=periodo,
    )[
        ["periodo", "valor"]
    ].rename(columns={"valor": "acumulado"})

    # Acumulado 12 meses (2265)
    df_acum12 = sidra_query(
        tabela=1737,
        variavel=2265,
        periodo=periodo,
    )[
        ["periodo", "valor"]
    ].rename(columns={"valor": "acumulado12m"})

    out = (
        df_indice.merge(df_acum, on="periodo")
        .merge(df_acum12, on="periodo")
        .merge(df_nindice, on="periodo")
    )

    out = out.rename(columns={"periodo": "date"})

    out["date"] = pd.to_datetime(
        out["date"],
        format="%Y%m",
    )

    return out[
        [
            "date",
            "indice",
            "acumulado",
            "acumulado12m",
            "nindice",
        ]
    ]


def run_ipca_geral(periodo="all"):
    df = get_ipca_geral(periodo)
    table = "ipca_geral"
    safe_replace(df, table)
    #    truncate_table("ipca_geral", schema="bcb")
    #    insert_all(df, "ipca_geral", schema="bcb")
    print("Tabela bcb.ipca_geral atualizada!")


def main():
    run_ipca_geral()


if __name__ == "__main__":
    main()
