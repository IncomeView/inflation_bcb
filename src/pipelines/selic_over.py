# src/pipelines/selic_over.py
from src.api.sgs_series import get_series
from src.database.load import insert_all, truncate_table


def run_selic_over():
    codigo = 11  # SELIC over
    df = get_series(codigo)
    df["series_id"] = codigo

    table = "selic_over"

    truncate_table(table)
    insert_all(df, table)


def main():
    run_selic_over()


if __name__ == "__main__":
    main()
