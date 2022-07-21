from models.user_node import User
import uvicorn
from fastapi import FastAPI
from dao.graph_dao import GraphDAO
from config.redis_conf import redis_connection as redis

app = FastAPI()


@app.on_event("startup")
async def commit_graphs():
    """ Generates the requiered graphs if they
    don't exist on the database
    """
    graph = redis.graph("users_followups")
    graph.commit()



@app.get("/nodes/{node_id}")
async def get_node_by_id(node_id: str):
    """ Given an id it returns the node

    Args:
        node_id (str)

    """
    return GraphDAO().get_node_by_id(node_id)


@app.get("/graph/")
async def get_graph(limit: int = 50):
    """ Returns a graph (nodes with all their relationships)

    Args:
        limit (int, optional): Amout of vertex to display. Defaults to 50.

    Returns:
        Graph: A graph
    """
    return GraphDAO().get_graph(limit)


@app.post("/node/")
async def create_node(node: User):
    """ Creates a new node, following the
    User model

    Args:
        node (User): User node according
        to the model

    Returns:
        Server response: Server responde
    """
    return GraphDAO().create_node(node)


@app.post("/edge/")
async def create_edge(node_follower_id: str, node_followed_id: str):
    """ Given two nodes, it creates an edge betweem
    them
    """
    return GraphDAO().create_edge(node_follower_id, node_followed_id)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8002, reload=True)
