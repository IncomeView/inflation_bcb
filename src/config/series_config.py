# Dados de início fixos para cada série, pois o SGS tem dados inconsistentes para datas muito antigas.
FIRST_DATES = {
    11: "01/01/2000",  # Selic Over (diária)
    432: "05/03/1999",  # Selic Meta
}


def get_first_date(codigo_serie: int) -> str:
    return FIRST_DATES[codigo_serie]
