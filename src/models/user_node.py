from pydantic import BaseModel
from redis.commands.graph.node import Node

class User(BaseModel):
    pk: str
    username: str
    age: int


    def __init__(self, pk, username, age):
        self.pk = pk
        self.username = username
        self.age = age


    def to_node(self):
        properties = dict(self)
        pk = properties.pop("pk")
        return Node(node_id=pk, label="User", properties=properties)
