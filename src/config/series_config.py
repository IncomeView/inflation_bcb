# src/config/series_config.py

SERIES_FIRST_DATE = {
    # SELIC
    432: "01/01/2000",  # SELIC meta (BCB/SGS)
    11: "01/01/2000",  # SELIC over (BCB/SGS - série antiga)
}


def get_first_date(codigo_serie: int) -> str:
    if codigo_serie not in SERIES_FIRST_DATE:
        raise ValueError(f"Série {codigo_serie} não configurada.")
    return SERIES_FIRST_DATE[codigo_serie]
