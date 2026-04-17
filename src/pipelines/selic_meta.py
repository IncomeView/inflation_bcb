from pathlib import Path
from src.config.series_config import get_first_date
from src.api.sgs_series import get_last_valid_date, get_bc_full_series


# Caminho absoluto para o diretório raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]   # volta até inflation/
DATA_RAW_DIR = ROOT_DIR / "data" / "raw"
DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)


# Pipeline para coletar a série da Selic Meta (código 432) do SGS e salvar em CSV.
def run_selic_meta():
    codigo = 432
    start = get_first_date(codigo)
    end = get_last_valid_date(codigo)

    df = get_bc_full_series(codigo, start, end)

    path = DATA_RAW_DIR / "selic_meta.csv"
    df.to_csv(path, index=False)

    print(f"Selic Meta salva em: {path}")
