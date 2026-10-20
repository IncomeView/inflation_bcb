# test_taxonomia.py

from src.domain.ipca.taxonomia import (
    get_bloco_macro,
)


def test_subitem_taxonomia():
    bloco = get_bloco_macro("5101001")
    assert bloco is not None
