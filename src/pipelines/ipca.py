from src.api.sgs_series import get_series
from src.database.load import ensure_table, insert_all


def run_ipca():
    df = get_series(433)
    df["series_id"] = 433

    table = "ipca"

    ensure_table(df, table)
    insert_all(df, table)


def main():
    run_ipca()


if __name__ == "__main__":
    main()
