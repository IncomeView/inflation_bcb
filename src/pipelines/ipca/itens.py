# src/pipelines/ipca/itens.py

from src.database.load import insert_all, truncate_table
from src.pipelines.ipca.base import get_ipca_nivel
from src.pipelines.ipca.codigos import cod_itens


def run_ipca_itens(periodo="all"):
    df = get_ipca_nivel(cod_itens, periodo)
    truncate_table("ipca_itens", schema="bcb")
    insert_all(df, "ipca_itens", schema="bcb")
    print("Tabela bcb.ipca_itens atualizada!")


def main():
    run_ipca_itens()


if __name__ == "__main__":
    run_ipca_itens()
