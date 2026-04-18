from src.config.series_config import SERIES

def test_series_config_structure():
    assert isinstance(SERIES, dict)
    assert "selic_over" in SERIES
    assert "selic_meta" in SERIES

def test_series_config_items():
    item = SERIES["selic_over"]
    assert "code" in item
    assert "name" in item
