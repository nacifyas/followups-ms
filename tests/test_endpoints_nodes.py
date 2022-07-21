from models.user_node import User
import requests
from fastapi import status


ROOT = "http://127.0.0.1:8002"


def test_endpoint_create_node():
    """ Test the creation of two
    nodes, using the endpoint
    http://127.0.0.1:8002/node/
    """
    endpoint = f"{ROOT}/node"
    node1 = User(**
        {
            "pk": "test_pk",
            "username": "test_username",
            "age": 10
        }
    )
    node2 = User(**
        {
            "pk": "test_pk2",
            "username": "test_username2",
            "age": 10
        }
    )
    r = requests.post(endpoint, data=node1.dict())
    r2 = requests.post(endpoint, data=node2.dict())
    assert r.status_code == status.HTTP_201_CREATED
    assert r2.status_code == status.HTTP_201_CREATED


def test_endpoint_fail_create_existing_node():
    """ Test if creating a duplicate
    primary key fails
    """
    endpoint = f"{ROOT}/node"
    existing_node = User(**
        {
            "pk": "test_pk",
            "username": "test_username",
            "age": 10
        }
    )
    r = requests.post(endpoint, data=existing_node.dict())
    assert r.status_code == status.HTTP_406_NOT_ACCEPTABLE


def test_create_edge():
    """ Test if creating an
    edge succeeds
    """
    pk1 = "test_pk"
    pk2 = "test_pk2"
    endpoint = f"{ROOT}/edge?node_follower_pk={pk1}&node_followed_pk={pk2}"
    r = requests.post(endpoint)
    assert r.status_code == status.HTTP_201_CREATED


def test_fail_create_edge_with_non_existing_node():
    """ Test if creating an
    edge with a non existing node,
    fails
    """
    pk1 = "test_pk"
    pk2 = "non_existing_pk"
    endpoint = f"{ROOT}/edge?node_follower_pk={pk1}&node_followed_pk={pk2}"
    r = requests.post(endpoint)
    assert r.status_code == status.HTTP_406_NOT_ACCEPTABLE


def test_endpoint_get_graph():
    """ Test to check if the endpoint
    http://127.0.0.1:8002/node/ 
    returns a 200 ok response
    """
    endpoint = f"{ROOT}/graph"
    r = requests.get(endpoint)
    assert r.status_code == status.HTTP_200_OK


def test_endpoint_get_node_by_primary_key():
    """ Test to check if the endpoint
    http://127.0.0.1:8002/node/{pk} 
    returns a 200 ok response
    """
    primary_key = "test_pk"
    endpoint = f"{ROOT}/node/{primary_key}"
    r = requests.get(endpoint)
    assert r.status_code == status.HTTP_200_OK


def test_endpoint_fail_get_no_existing_node_by_primary_key():
    """ Test cheking if fails
    returning a non-existing node
    """
    primary_key = "non_existing_pk"
    endpoint = f"{ROOT}/node/{primary_key}"
    r = requests.get(endpoint)
    assert r.status_code == status.HTTP_404_NOT_FOUND


def test_endpoint_delete_edge():
    """ Test deleting an edge
    """
    pk1 = "test_pk"
    pk2 = "test_pk2"
    endpoint = f"{ROOT}/edge?node_follower_pk={pk1}&node_followed_pk={pk2}"
    r = requests.delete(endpoint)
    assert r.status_code == status.HTTP_202_ACCEPTED


def test_endpoint_delete_node():
    """ Test deleting a node
    """
    pk1 = "test_pk"
    pk2 = "test_pk2"
    endpoint = f"{ROOT}/edge?node_pk={pk1}"
    r1 = requests.delete(endpoint)
    endpoint = f"{ROOT}/edge?node_pk={pk2}"
    r2 = requests.delete(endpoint)
    assert r1.status_code == status.HTTP_202_ACCEPTED
    assert r2.status_code == status.HTTP_202_ACCEPTED
