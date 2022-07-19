from pprint import pprint
from config.neo4j_conf import init_db
from models.graph_model import UserNode, UserCreate


def normalize(user_node: UserNode) -> dict[str:str]:
    pass

class GraphDAL():

    def get_nodes(self, limit: int = 0) -> list[UserNode]:
        nodes: list[UserNode] = UserNode.nodes.all()
        return [nd for nd in nodes]


    def get_node_by_uid(self, uid: str):
        return UserNode.nodes.get(uid=uid)


    def create_node(self, user: UserCreate) -> UserNode:
        return UserNode(**dict(user)).save()


    def create_relation(self, user_uid: str, new_user_uid: str):
        user: UserNode = UserNode.nodes.get(uid=user_uid)
        new_user: UserNode = UserNode.nodes.get(uid=new_user_uid)
        pprint(user)
        rel = user.follows.connect(new_user)
        rel.save()


    def delete_user(self, uid) -> None:
        UserNode.delete(UserNode.nodes.get(uid=uid))


    def delete_relation(self, uid) -> None:
        pass
 
init_db()
print(GraphDAL().get_nodes())