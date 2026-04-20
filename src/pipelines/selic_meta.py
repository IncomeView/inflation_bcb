from src.api.sgs_series import get_series
from src.database.load import ensure_table, insert_all


def run_selic_meta():
    df = get_series(432)
    df["series_id"] = 432

    table = "selic_meta"

    ensure_table(df, table)
    insert_all(df, table)


def main():
    run_selic_meta()


if __name__ == "__main__":
    main()
