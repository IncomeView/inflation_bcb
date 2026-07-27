# src/config/series_config.py

SERIES = {
    "selic_over": {
        "code": 11,
        "first_date": "01/01/2000",
    },
    "selic_meta": {
        "code": 432,
        "first_date": "01/01/2000",
    },
    "ipca_geral": {
        "code": 1737,
        "first_date": "01/01/1980",
    },
    "ipca_grupos": {
        "code": 7060,
        "first_date": "01/01/1980",
    },
}


def get_first_date(codigo_serie: int) -> str:
    for item in SERIES.values():
        if item["code"] == codigo_serie:
            return item["first_date"]
    raise ValueError(f"Série {codigo_serie} não configurada.")
