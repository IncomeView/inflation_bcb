# test_ipca_taxonomia.py

from src.domain.ipca.taxonomia import (
    CLASSIFICACAO_SUBGRUPOS,
)


def test_taxonomia_tem_subgrupos():
    assert len(CLASSIFICACAO_SUBGRUPOS) > 0
