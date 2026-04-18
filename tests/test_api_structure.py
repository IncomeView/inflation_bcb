from src.api.bcb_client import BCBClient

def test_bcb_client_has_get_method():
    client = BCBClient()
    assert hasattr(client, "get_series")

def test_bcb_client_init():
    client = BCBClient()
    assert client is not None
