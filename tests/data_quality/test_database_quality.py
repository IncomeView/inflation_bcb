# test_database_quality.py

import pandas as pd
import pytest

from src.database.connection import engine

pytestmark = pytest.mark.database


def test_ipca_geral_not_empty():
    df = pd.read_sql(
        "select * from bcb.ipca_geral limit 1",
        engine,
    )
    assert len(df) > 0


def test_ipca_sem_data_futura():
    df = pd.read_sql(
        """
        select max(date) as max_date
        from bcb.ipca_geral
        """,
        engine,
    )
    assert pd.to_datetime(df["max_date"][0]) <= pd.Timestamp.today()


def test_ipca_subitens_sem_duplicatas():
    df = pd.read_sql(
        """
        select
            date,
            categoria,
            count(*) qtd
        from bcb.ipca_subitens
        group by date,categoria
        having count(*) > 1
        """,
        engine,
    )
    assert len(df) == 0


def test_taxonomia_sem_nulos():
    df = pd.read_sql(
        """
        select *
        from bcb.ipca_taxonomia
        where bloco_macro is null
        """,
        engine,
    )
    assert len(df) == 0
