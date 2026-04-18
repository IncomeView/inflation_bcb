import src.pipelines.selic_over as selic_over
import src.pipelines.selic_meta as selic_meta

def test_selic_over_has_main():
    assert hasattr(selic_over, "main")

def test_selic_meta_has_main():
    assert hasattr(selic_meta, "main")
