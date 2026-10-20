# health_check.py

import pandas as pd

from src.database.connection import engine

TABLES = [
    "ipca_geral",
    "ipca_subitens",
    "ipca_taxonomia",
    "selic_meta",
    "selic_over",
]


def validate_database():
    output = {}
    for table in TABLES:
        try:
            df = pd.read_sql(
                f"""
                SELECT COUNT(*) AS rows
                FROM bcb.{table}
                """,
                engine,
            )
            output[table] = {
                "status": "OK",
                "rows": int(df.iloc[0]["rows"]),
            }

        except Exception as e:
            output[table] = {
                "status": "ERROR",
                "message": str(e),
            }

    return output
