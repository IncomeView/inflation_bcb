# test_validation.py

import pandas as pd

from src.core.validate import validate_df


def test_empty_dataframe():
    df = pd.DataFrame()
    try:
        validate_df(df)
        assert False
    except ValueError:
        assert True


def test_missing_columns():
    df = pd.DataFrame(
        {
            "date": ["2024-01-01"],
            "indice": [0.42],
        }
    )
    try:
        validate_df(
            df,
            required_cols=[
                "date",
                "indice",
                "acumulado12m",
            ],
        )
        assert False
    except ValueError:
        assert True


def test_valid_dataframe():
    df = pd.DataFrame(
        {
            "date": ["2024-01-01"],
            "indice": [0.42],
            "acumulado12m": [4.56],
        }
    )
    assert (
        validate_df(
            df,
            required_cols=[
                "date",
                "indice",
                "acumulado12m",
            ],
        )
        is True
    )
