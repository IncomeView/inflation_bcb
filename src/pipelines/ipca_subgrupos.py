import pandas as pd

from src.api.sidra_client import sidra_query
from src.database.load import ensure_table, insert_all

# ============================================================
# 1. Funções auxiliares (pipeline)
# ============================================================


def load_ipca_raw(periodo="all"):
    """Consulta os dados brutos do SIDRA para valor e peso."""
    df_valor = sidra_query(
        tabela=7060,
        variavel=63,  # variação mensal (%)
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "indice"})

    df_peso = sidra_query(
        tabela=7060,
        variavel=66,  # peso mensal (%)
        periodo=periodo,
        classificacao={"315": "all"},
    ).rename(columns={"valor": "peso"})

    return df_valor.copy(), df_peso.copy()


def filter_level_5(df):
    """Filtra somente SUBGRUPOS (nível 5)."""
    df = df.copy()
    df["nivel"] = df["categoria"].apply(lambda x: len(str(x).split(".")[0]))
    return df[df["nivel"] == 2].copy()


def merge_valor_peso(df_valor, df_peso):
    """Une valor e peso em um único dataframe."""
    return df_valor.merge(
        df_peso[["periodo", "categoria", "peso"]],
        on=["periodo", "categoria"],
        how="left",
        validate="one_to_one",
    )


def split_category(df):
    """Separa category (código) e category_name (nome)."""
    df = df.copy()
    df["category"] = df["categoria"].apply(lambda x: str(x).split(".")[0])
    df["category_name"] = df["categoria"].apply(
        lambda x: str(x).split(".")[1] if "." in str(x) else None
    )
    return df


def format_output(df):
    """Formata a tabela final com as colunas desejadas."""
    df = df.rename(columns={"periodo": "date"})

    # Conversão correta: YYYYMM → datetime
    df["date"] = pd.to_datetime(df["date"], format="%Y%m")

    df = df[["date", "indice", "peso", "category", "category_name"]].copy()
    return df


# ============================================================
# 2. Função principal de dados
# ============================================================


def get_ipca_subgrupos(periodo="all"):
    """Retorna o DataFrame final de IPCA subgrupos (nível 5)."""

    df_valor, df_peso = load_ipca_raw(periodo)

    df_valor = filter_level_5(df_valor)
    df_peso = filter_level_5(df_peso)

    df = merge_valor_peso(df_valor, df_peso)
    df = split_category(df)
    df = format_output(df)

    return df


# ============================================================
# 3. Função pipeline (grava no banco)
# ============================================================


def run_ipca_subgrupos(periodo="all"):
    """
    Executa o pipeline do IPCA subgrupos:
    - consulta o SIDRA (tabela 7060)
    - monta o DataFrame com Indice, Peso e categorias
    - cria/atualiza a tabela bcb.ipca_subgrupos
    """
    df = get_ipca_subgrupos(periodo)

    ensure_table(df, "ipca_subgrupos", schema="bcb")
    insert_all(df, "ipca_subgrupos", schema="bcb")

    print("Tabela bcb.ipca_subgrupos atualizada com sucesso!")

    return df


# ============================================================
# 4. Execução direta
# ============================================================

if __name__ == "__main__":
    run_ipca_subgrupos()
