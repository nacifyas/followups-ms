from pprint import pprint
from config.neo4j_conf import init_db
from models.graph_model import UserNode, UserCreate

class GraphDAL():

    def get_graph(self, limit: int = 0):
        nodes = UserNode.nodes.all()[:limit]
        print(nodes)
        return nodes


    def get_node(self, uid: str):
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
 