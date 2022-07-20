import uvicorn
from fastapi import FastAPI
from dao.graph_dao import GraphDAO

app = FastAPI()


@app.get("/nodes/")
async def get_nodes(offset: int = 0, limit: int = 50):
    """ Returns list of all nodes, skipping the amount
    specified by the offset, and limited by the argument
    limit

    Args:
        limit (int, optional): _description_. Defaults to 50.

    Returns:
        list[Node]: list of all nodes
    """
    return await GraphDAO().get_nodes(offset, limit)


@app.get("/graph/")
async def get_graph(limit: int = 50):
    """ Returns a graph (nodes with all their relationships)

    Args:
        limit (int, optional): Amout of vertex to display. Defaults to 50.

    Returns:
        Graph: A graph
    """
    return await GraphDAO().get_graph(limit)


@app.get("/nodes/{node_id}")
async def get_node_neighbours(node_id: str):
    """
    Given a node id, it returns a list with all nodes
    connected to it

    Args:
        node_id (str): Node id

    Returns:
        List[Node]:  A list with all nodes connected to it
    """
    return await GraphDAO().get_node_neighbours(node_id)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8002, reload=True)
