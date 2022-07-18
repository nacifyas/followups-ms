import uvicorn
from fastapi import FastAPI
from config.neo4j_conf import init_db
from dal.graph import GraphDAL


app = FastAPI()

@app.on_event("startup")
async def _init_neo4j_():
    init_db()


@app.get("/")
async def get_graph(offset: int = 0, limit: int = 50):
    return GraphDAL().get_graph(offset, limit)


@app.get("/users/{username}")
async def get_graph_centered_on_node(username: str):
    return GraphDAL().get_graph_centered_on_node(username)


@app.post("/users/")
async def create_node(user):
    return GraphDAL().create_node(user)


@app.post("/relations/")
async def create_relation(user):
    return GraphDAL().create_relation(user)

@app.delete("/users/{id}")
async def delete_user(id):
    return GraphDAL().delete_user(id)


@app.delete("/relations/{id}")
async def delete_relation(id):
    return GraphDAL().delete_relation(id)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8002, reload=True)
