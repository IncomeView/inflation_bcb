SERIES = {
    "selic_over": {
        "code": 11,
        "name": "Selic Over",
        "first_date": "01/01/2000",
    },
    "selic_meta": {
        "code": 432,
        "name": "Selic Meta",
        "first_date": "05/03/1999",
    },
    "ipca": {
        "code": 433,
        "name": "ipca",
        "first_date": "01/01/1980",
    },
}

SERIES_CONFIG = {
    11: {"name": "SELIC over", "update": "incremental"},
    432: {"name": "SELIC meta", "update": "incremental"},
    433: {"name": "IPCA", "update": "incremental"},  # IPCA geral
    444: {
        "name": "IPCA grupos",
        "update": "truncate",
    },  # IPCA por grupos (alimentação, habitação, etc)
    445: {
        "name": "IPCA Habitação (grupo)",
        "update": "truncate",
    },  # IPCA habitação (grupo)
}


def get_first_date(codigo_serie: int) -> str:
    # Busca a série pelo código
    for item in SERIES.values():
        if item["code"] == codigo_serie:
            return item["first_date"]
    raise KeyError(f"Série não encontrada para código {codigo_serie}")
