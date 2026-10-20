# test_series_config.py

from src.config.series_config import (
    SERIES,
)


def test_series_codes():
    assert SERIES["selic_meta"]["code"] == 432
    assert SERIES["selic_over"]["code"] == 11
