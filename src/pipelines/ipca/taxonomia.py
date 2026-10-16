# src/pipelines/ipca/taxonomia.py

import pandas as pd

from src.config.ipca_taxonomia import (
    get_bloco_macro,
    get_categoria_cidada,
)
from src.database.connection import engine
from src.database.load import (
    insert_all,
    truncate_table,
)

TABLE_NAME = "ipca_taxonomia"


def build_taxonomia():
    df = pd.read_sql(
        """
        SELECT DISTINCT
            categoria AS subitem_id
        FROM bcb.ipca_subitens
        ORDER BY categoria
        """,
        engine,
    )

    df["subitem_id"] = df["subitem_id"].astype(str)
    df["bloco_macro"] = df["subitem_id"].apply(get_bloco_macro)
    df["categoria_cidada"] = df["subitem_id"].apply(get_categoria_cidada)
    df["sub_bloco"] = None
    df["subcategoria_cidada"] = None

    return df


def validate_taxonomia(df):
    missing_macro = df["bloco_macro"].isna().sum()
    missing_cidada = df["categoria_cidada"].isna().sum()

    if missing_macro:
        print("\nSubitens sem bloco macro:\n")
        print(df[df["bloco_macro"].isna()][["subitem_id"]])

        raise ValueError(f"{missing_macro} subitens sem bloco macro.")

    if missing_cidada:
        print("\nSubitens sem categoria cidadã:\n")
        print(df[df["categoria_cidada"].isna()][["subitem_id"]])

        raise ValueError(f"{missing_cidada} subitens sem categoria cidadã.")


def run_taxonomia():
    df = build_taxonomia()
    validate_taxonomia(df)

    truncate_table(
        TABLE_NAME,
        schema="bcb",
    )
    insert_all(
        df,
        TABLE_NAME,
        schema="bcb",
    )

    print(f"Tabela bcb.{TABLE_NAME} atualizada.")


def main():
    run_taxonomia()


if __name__ == "__main__":
    main()
