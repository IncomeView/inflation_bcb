# src/config/series_config.py# src/config/series_config.py

SERIES = {
    "ipca_geral": 1737,
    "ipca_grupos": 7060,
    "selic_meta": 432,
    "selic_over": 11,
}

SERIES_FIRST_DATE = {
    432: "01/01/2000",
    11: "01/01/2000",
}


def get_first_date(codigo_serie: int) -> str:
    if codigo_serie not in SERIES_FIRST_DATE:
        raise ValueError(f"Série {codigo_serie} não configurada.")
    return SERIES_FIRST_DATE[codigo_serie]
