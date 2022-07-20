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
        list[UserNode]: _description_
    """
    return GraphDAO().get_nodes(offset, limit)



if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8002, reload=True)
