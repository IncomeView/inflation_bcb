# src/pipelines/selic_over.py
from src.api.sgs_series import get_series
from src.database.load import safe_replace


def run_selic_over():
    codigo = 11  # SELIC over
    df = get_series(codigo)
    df["series_id"] = codigo
    table = "selic_over"

    safe_replace(df, table)


def main():
    run_selic_over()


if __name__ == "__main__":
    main()
