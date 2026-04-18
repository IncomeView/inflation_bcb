from pathlib import Path

from src.api.sgs_series import get_bc_full_series, get_last_valid_date
from src.config.series_config import get_first_date
from src.utils.logging import get_logger

logger = get_logger(__name__)

# Caminho absoluto para o diretório raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]  # volta até inflation/
DATA_RAW_DIR = ROOT_DIR / "data" / "raw"
DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)


def run_selic_over():
    codigo = 11
    start = get_first_date(codigo)
    end = get_last_valid_date(codigo)

    df = get_bc_full_series(codigo, start, end)

    path = DATA_RAW_DIR / "selic_over.csv"
    df.to_csv(path, index=False)

    logger.info(f"Arquivo salvo com sucesso em: {path}")


def main():
    run_selic_over()
