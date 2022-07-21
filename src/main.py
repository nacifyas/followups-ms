from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException, Response, status
from models.user_node import User
from dao.graph_dao import GraphDAO
from config.redis_conf import redis_connection as redis

app = FastAPI()


@app.on_event("startup")
async def commit_graphs():
    """ Generates the requiered graphs if they
    do not exist on the database
    """
    graph = redis.graph("users_followups")
    graph.commit()


@app.get("/node/{primary_key}", status_code=status.HTTP_200_OK)
async def get_node_by_primary_key(primary_key: str) -> list:
    """ Given a primary key this endpoint will return
    its corresponding node

    Args:
        primary_key (str): Entity primary key

    Raises:
        HTTPException: 404 error if such node
        is not found

    Returns:
        list: A list containing the graph's entity data
    """
    node = GraphDAO().get_node_by_primary_key(primary_key)
    if len(node) > 0:
        return node
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Node not found"
        )


@app.get("/graph/", status_code=status.HTTP_200_OK)
async def get_graph() -> list:
    """ Returns a graph (nodes with all their relationships)
    whithin a list


    Returns:
        list: List with nodes and edges
    """
    return GraphDAO().get_graph()


@app.post("/node/", status_code=status.HTTP_201_CREATED)
async def create_node(node: User) -> Response:
    """ Creates a new node, following the
    User model

    Args:
        node (User): User node according
        to the model

    Raises:
        HTTPException: Error 406 if the provided
        primary key already exists

    Returns:
        Response: HTTP 201 created
    """
    nd = GraphDAO().get_node_by_primary_key(node.pk)
    if len(nd) > 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Primary key already exists"
        )
    GraphDAO().create_node(node)
    return Response(
        content="Created",
        status_code=status.HTTP_201_CREATED
    )


@app.post("/edge/", status_code=status.HTTP_201_CREATED)
async def create_edge(node_follower_pk: str, node_followed_pk: str, properties: dict = { "date time": datetime.now() }) -> Response:
    """ Given two nodes by their primary keys, this creates and edge
    betweem them with the provided properties

    Args:
        node_follower_pk (str): Primary key of the follower node
        node_followed_pk (str): Primary key of the followed node
        properties (dict, optional): Dictionary with properties
        to store in the edge. Defaults to { "date time": datetime.now() }.

    Raises:
        HTTPException: 406 error if any of the specified nodes
        do not exist

    Returns:
        Response: HTTP 201 created
    """
    nodes: list = GraphDAO().get_node_by_primary_key(node_follower_pk)
    nodes.extend(GraphDAO().get_node_by_primary_key(node_followed_pk))
    if len(nodes) < 2:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Node not found"
        )
    GraphDAO().create_edge(node_follower_pk, node_followed_pk, properties)
    return Response(
        content="Created",
        status_code=status.HTTP_201_CREATED
    )


@app.delete("/node/{primary_key}", status_code=status.HTTP_202_ACCEPTED)
async def delete_edge(primary_key: str) -> Response:
    """ Given a node pk, it will
    delete it from the graph

    Args:
        edge_pk (str): pk if the edge
    """
    GraphDAO().delete_node(primary_key)
    return Response(
        content="Deleted",
        status_code=status.HTTP_202_ACCEPTED
    )


@app.delete("/edge/", status_code=status.HTTP_202_ACCEPTED)
async def delete_edge(node1_primary_key: str, node2_primary_key: str) -> Response:
    """ Given an edge pk, it will
    delete it from the graph

    Args:
        edge_pk (str): pk if the edge
    """
    GraphDAO().delete_edge(node1_primary_key, node2_primary_key)
    return Response(
        content="Deleted",
        status_code=status.HTTP_202_ACCEPTED
    )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8002, reload=True)
