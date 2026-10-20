# src/pipelines/selic_meta.py
from src.api.sgs_series import get_series
from src.database.load import safe_replace


def run_selic_meta():
    codigo = 432  # SELIC meta
    df = get_series(codigo)
    df["series_id"] = codigo
    table = "selic_meta"

    safe_replace(df, table)


def main():
    run_selic_meta()


if __name__ == "__main__":
    main()
