from src.database.load import insert_all, truncate_table
from src.pipelines.ipca.base import get_ipca_nivel
from src.pipelines.ipca.codigos import cod_grupos


def run_ipca_grupos(periodo="all"):
    """
    Executa o pipeline do IPCA grupos usando a tabela 7060 (classificação 315).
    """
    df = get_ipca_nivel(cod_grupos, periodo)
    truncate_table("ipca_grupos", schema="bcb")
    insert_all(df, "ipca_grupos", schema="bcb")
    print("Tabela bcb.ipca_grupos atualizada!")


def main():
    run_ipca_grupos()


if __name__ == "__main__":
    run_ipca_grupos()
