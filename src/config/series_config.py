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
}

def get_first_date(codigo_serie: int) -> str:
    # Busca a série pelo código
    for item in SERIES.values():
        if item["code"] == codigo_serie:
            return item["first_date"]
    raise KeyError(f"Série não encontrada para código {codigo_serie}")
