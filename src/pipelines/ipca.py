from src.api.ipca_series import get_ipca_geral
from src.database.load import ensure_table, insert_all


def run_ipca():
    """
    Executa o pipeline do IPCA geral:
    - consulta o SIDRA (tabela 1737)
    - monta o DataFrame com as 4 variáveis principais
    - cria/atualiza a tabela bcb.ipca
    """
    df = get_ipca_geral()

    ensure_table(df, "ipca", schema="bcb")
    insert_all(df, "ipca", schema="bcb")

    print("Tabela bcb.ipca atualizada com sucesso!")


if __name__ == "__main__":
    run_ipca()
