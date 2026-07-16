# src/pipelines/selic_meta.py
from src.api.sgs_series import get_series
from src.database.load import insert_all, truncate_table


def run_selic_meta():
    codigo = 432  # SELIC meta
    df = get_series(codigo)
    df["series_id"] = codigo

    table = "selic_meta"

    truncate_table(table)
    insert_all(df, table)


def main():
    run_selic_meta()


if __name__ == "__main__":
    main()
