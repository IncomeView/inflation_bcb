import pandas as pd

from src.api.sidra_client import sidra_query
from src.database.load import insert_all, truncate_table


def load_ipca_raw(periodo="all"):
    df_valor = sidra_query(
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

    return df_valor.copy(), df_peso.copy()


def filter_level_2(df):
    df = df.copy()
    df["nivel"] = df["categoria"].apply(lambda x: len(str(x).split(".")[0]))
    return df[df["nivel"] == 1].copy()


def merge_valor_peso(df_valor, df_peso):
    return df_valor.merge(
        df_peso[["periodo", "categoria", "peso"]],
        on=["periodo", "categoria"],
        how="left",
        validate="one_to_one",
    )


def split_category(df):
    df = df.copy()
    df["category"] = df["categoria"].apply(lambda x: str(x).split(".")[0])
    df["category_name"] = df["categoria"].apply(
        lambda x: str(x).split(".")[1] if "." in str(x) else None
    )
    return df


def format_output(df):
    df = df.rename(columns={"periodo": "date"})
    df["date"] = pd.to_datetime(df["date"], format="%Y%m")
    return df[["date", "indice", "peso", "category", "category_name"]].copy()


def get_ipca_grupos(periodo="all"):
    df_valor, df_peso = load_ipca_raw(periodo)
    df_valor = filter_level_2(df_valor)
    df_peso = filter_level_2(df_peso)
    df = merge_valor_peso(df_valor, df_peso)
    df = split_category(df)
    df = format_output(df)
    return df


def run_ipca_grupos(periodo="all"):
    df = get_ipca_grupos(periodo)
    truncate_table("ipca_grupos", schema="bcb")
    insert_all(df, "ipca_grupos", schema="bcb")
    print("Tabela bcb.ipca_grupos atualizada com sucesso!")


if __name__ == "__main__":
    run_ipca_grupos()
