# src/pipelines/run_all.py

from src.pipelines.ipca.geral import run_ipca_geral
from src.pipelines.ipca.grupos import run_ipca_grupos
from src.pipelines.ipca.itens import run_ipca_itens
from src.pipelines.ipca.subgrupos import run_ipca_subgrupos
from src.pipelines.ipca.subitens import run_ipca_subitens
from src.pipelines.selic_meta import run_selic_meta
from src.pipelines.selic_over import run_selic_over


def run_all():
    run_ipca_geral()
    run_ipca_grupos()
    run_ipca_subgrupos()
    run_ipca_itens()
    run_ipca_subitens()

    run_selic_meta()
    run_selic_over()


def main():
    run_all()


if __name__ == "__main__":
    main()
