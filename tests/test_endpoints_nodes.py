import requests
from fastapi import status

ROOT = "http://127.0.0.1:8002"

def test_endpoint_get_nodes():
    """ Test to check if the endpoint
    http://127.0.0.1:8002/nodes/ return
    a 200 ok response
    """
    endpoint = f"{ROOT}/nodes/"
    r = requests.get(endpoint)
    assert r.status_code == status.HTTP_200_OK