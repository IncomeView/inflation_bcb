# grupos.py

from src.database.load import insert_all, truncate_table
from src.pipelines.ipca.base import get_ipca_nivel


def run_ipca_grupos(periodo="all"):
    df = get_ipca_nivel(prefix_len=1, periodo=periodo)
    truncate_table("ipca_grupos", schema="bcb")
    insert_all(df, "ipca_grupos", schema="bcb")
    print("Tabela bcb.ipca_grupos atualizada!")


def main():
    run_ipca_grupos()


if __name__ == "__main__":
    run_ipca_grupos()
