import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import Response
from config.neo4j_conf import init_db
from dal.graph import GraphDAL
from neomodel import DoesNotExist, UniqueProperty

from models.graph_model import UserCreate
from models.graph_model import UserNode 

app = FastAPI()

@app.on_event("startup")
async def _init_neo4j_():
    init_db()


@app.get("/")
async def get_nodes(limit: int = 50) -> list[UserNode]:
    return GraphDAL().get_nodes(limit)


@app.get("/{uid}")
async def get_node_by_uid(uid: str) -> UserNode:
    try:
        return GraphDAL().get_node_by_uid(uid)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Node not found"
        )


@app.post("/users/")
async def create_node(user: UserCreate) -> UserNode:
    try:
        return GraphDAL().create_node(user)
    except UniqueProperty as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=e.message
        )


@app.post("/relations/")
async def create_relation(relation: tuple[str, str]):
    user_uid, new_user_uid = relation
    GraphDAL().create_relation(user_uid, new_user_uid)


@app.delete("/users/{uid}")
async def delete_user(uid: str) -> Response:
    try:
        GraphDAL().delete_user(uid)
        return Response(
            status_code=status.HTTP_204_NO_CONTENT
        )
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Node not found"
        )


@app.delete("/relations/{uid}")
async def delete_relation(uid: str) -> Response:
    try:
        GraphDAL().delete_(uid)
        return Response(
            status_code=status.HTTP_202_ACCEPTED,
            content="Deleted"
        )
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Node not found"
        )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8002, reload=True)
