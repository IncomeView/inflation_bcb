from src.api.sgs_series import get_series
from src.database.load import ensure_table, insert_all, truncate_table


def run_selic_over():
    df = get_series(11)
    df["series_id"] = 11

    table = "selic_over"

    ensure_table(df, table)  # cria tabela se não existir
    truncate_table(table)  # limpa tudo
    insert_all(df, table)  # insere tudo de novo


def main():
    run_selic_over()


if __name__ == "__main__":
    main()
