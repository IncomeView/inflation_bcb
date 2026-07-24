# src/pipelines/ipca/subgrupos.py

from src.database.load import insert_all, truncate_table
from src.pipelines.ipca.base import get_ipca_nivel
from src.pipelines.ipca.codigos import cod_subgrupos


def run_ipca_subgrupos(periodo="all"):
    df = get_ipca_nivel(cod_subgrupos, periodo)
    truncate_table("ipca_subgrupos", schema="bcb")
    insert_all(df, "ipca_subgrupos", schema="bcb")
    print("Tabela bcb.ipca_subgrupos atualizada!")


def main():
    run_ipca_subgrupos()


if __name__ == "__main__":
    run_ipca_subgrupos()
