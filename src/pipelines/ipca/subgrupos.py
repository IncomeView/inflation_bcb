# src/pipelines/ipca/subgrupos.py

from src.database.load import safe_replace
from src.pipelines.ipca.base import get_ipca_nivel


def run_ipca_subgrupos(periodo="all"):
    df = get_ipca_nivel(prefix_len=2, periodo=periodo)
    table = "ipca_subgrupos"
    safe_replace(df, table)
    #    truncate_table("ipca_subgrupos", schema="bcb")
    #    insert_all(df, "ipca_subgrupos", schema="bcb")
    print("Tabela bcb.ipca_subgrupos atualizada!")


def main():
    run_ipca_subgrupos()


if __name__ == "__main__":
    run_ipca_subgrupos()
