from src.api.sgs_series import get_series
from src.database.load import ensure_table, insert_all, truncate_table


def run_selic_meta():
    df = get_series(432)
    df["series_id"] = 432

    table = "selic_meta"

    ensure_table(df, table)  # cria tabela se não existir
    truncate_table(table)  # limpa tudo
    insert_all(df, table)  # insere tudo de novo


def main():
    run_selic_meta()


if __name__ == "__main__":
    main()
