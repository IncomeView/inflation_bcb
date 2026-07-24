# src/pipelines/ipca/subitens.py

from src.database.load import insert_all, truncate_table
from src.pipelines.ipca.base import get_ipca_nivel
from src.pipelines.ipca.codigos import cod_subitens


def run_ipca_subitens(periodo="all"):
    df = get_ipca_nivel(cod_subitens, periodo)
    truncate_table("ipca_subitens", schema="bcb")
    insert_all(df, "ipca_subitens", schema="bcb")
    print("Tabela bcb.ipca_subitens atualizada!")


def main():
    run_ipca_subitens()


if __name__ == "__main__":
    run_ipca_subitens()
