# src/pipelines/ipca/subitens.py

from src.database.load import insert_all, truncate_table
from src.pipelines.ipca.base import get_ipca_nivel
from src.pipelines.ipca.codigos import cod_detalhados


def run_ipca_subitens_detalhados(periodo="all"):
    df = get_ipca_nivel(cod_detalhados, periodo)
    truncate_table("ipca_subitens_detalhados", schema="bcb")
    insert_all(df, "ipca_subitens_detalhados", schema="bcb")
    print("Tabela bcb.ipca_subitens_detalhados atualizada!")


def main():
    run_ipca_subitens_detalhados()


if __name__ == "__main__":
    run_ipca_subitens_detalhados()
