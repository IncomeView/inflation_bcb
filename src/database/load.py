# load.py

import pandas as pd
from sqlalchemy import text

from src.core.validate import validate_df
from src.database.connection import engine


def safe_replace(
    df,
    table,
    schema="bcb",
):
    validate_df(df)
    truncate_table(
        table,
        schema=schema,
    )
    insert_all(
        df,
        table,
        schema=schema,
    )


# -------------------------------------
# INSERT ALL (append)
# -------------------------------------
def insert_all(df: pd.DataFrame, table: str, schema: str = "bcb"):
    df.to_sql(table, engine, schema=schema, if_exists="append", index=False)


# -------------------------------------
# TRUNCATE TABLE
# -------------------------------------
def truncate_table(table: str, schema: str = "bcb"):
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {schema}.{table};"))
