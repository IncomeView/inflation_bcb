# src/pipelines/ipca/geral.py

from src.api.ipca_series import get_ipca_geral
from src.database.load import insert_all, truncate_table


def run_ipca_geral(periodo="all"):
    """
    Executa o pipeline do IPCA geral:
    - consulta o SIDRA (tabela 1737)
    - monta o DataFrame com as 4 variáveis principais
    - cria/atualiza a tabela bcb.ipca
    """
    df = get_ipca_geral(periodo)
    df["series_id"] = "ipca"

    table = "ipca"

    truncate_table(table, schema="bcb")
    insert_all(df, table, schema="bcb")

    print("Tabela bcb.ipca atualizada com sucesso!")


def main():
    run_ipca_geral()


if __name__ == "__main__":
    main()
