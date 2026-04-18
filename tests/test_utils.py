from src.utils.cache import Cache

def test_cache_initialization():
    c = Cache()
    assert hasattr(c, "path")

def test_cache_has_default_path():
    c = Cache()
    assert isinstance(c.path, str)
