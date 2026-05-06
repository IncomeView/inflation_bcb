import os

import pandas as pd
from sqlalchemy import inspect, text

from src.database.connection import engine


# -------------------------------------
# Verifica se tabela existe
# -------------------------------------
def table_exists(table: str, schema: str = "bcb") -> bool:
    inspector = inspect(engine)
    return inspector.has_table(table, schema=schema)


# -------------------------------------
# CREATE OR REPLACE TABLE
# -------------------------------------
def create_or_replace(df: pd.DataFrame, table: str, schema: str = "bcb"):
    df.to_sql(table, engine, schema=schema, if_exists="replace", index=False)


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


# -------------------------------------
# CRIAR TABELA SE NÃO EXISTIR
# -------------------------------------
def ensure_table(df: pd.DataFrame, table: str, schema: str = "bcb"):
    inspector = inspect(engine)

    # tabela existe?
    if inspector.has_table(table, schema=schema):
        return  # nada a fazer

    # cria tabela com as colunas do DataFrame
    df.head(0).to_sql(table, engine, schema=schema, if_exists="replace", index=False)


# -------------------------------------
# ATUALIZAR VIEWS BANCO bcb
# -------------------------------------
def load_views():
    views_path = os.path.join(os.path.dirname(__file__), "views")

    with engine.begin() as conn:
        conn.execute(text('SET search_path TO bcb;'))  # <<<<<< AQUI
        for file in os.listdir(views_path):
            if file.endswith(".sql"):
                sql_file = os.path.join(views_path, file)
                with open(sql_file, "r") as f:
                    sql = f.read()
                    conn.execute(text(sql))
                    print(f"View carregada: {file}")
