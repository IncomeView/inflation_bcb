# src/pipelines/ipca/itens.py

from src.database.load import safe_replace
from src.pipelines.ipca.base import get_ipca_nivel


def run_ipca_itens(periodo="all"):
    df = get_ipca_nivel(prefix_len=4, periodo=periodo)
    table = "ipca_itens"
    safe_replace(df, table)
    #    truncate_table("ipca_itens", schema="bcb")
    #    insert_all(df, "ipca_itens", schema="bcb")
    print("Tabela bcb.ipca_itens atualizada!")


def main():
    run_ipca_itens()


if __name__ == "__main__":
    run_ipca_itens()
