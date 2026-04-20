from src.api.sgs_series import get_series
from src.database.load import ensure_table, insert_all


def run_selic_over():
    df = get_series(11)
    df["series_id"] = 11

    table = "selic_over"

    ensure_table(df, table)
    insert_all(df, table)


def main():
    run_selic_over()


if __name__ == "__main__":
    main()
