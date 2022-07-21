from datetime import datetime
from config.redis_conf import redis_connection as redis
from models.user_node import User
from redis.commands.graph import Graph


class GraphDAO():
    graph: Graph

    def __init__(self, graph: Graph = redis.graph("users_followups")):
        self.graph = graph

    def get_node_by_primary_key(self, primary_key: str):
        query = f"MATCH (user:User) WHERE user.pk = '{primary_key}' RETURN user"
        return self.query_graph(query)

    def get_graph(self):
        query = f"MATCH (g) RETURN g"
        return self.query_graph(query)


    def create_node(self, node: User):
        self.graph.add_node(node.to_node())
        return self.graph.commit().result_set[0]


    def create_edge(self, node_follower_pk: str, node_followed_pk: str, properties: dict = {"date time":datetime.now()}):
        follower = "(follower:User {pk: '%s'})" % node_follower_pk
        followed = "(followed:User {pk: '%s'})" % node_followed_pk
        followup_data = str(properties)
        query = f"MATCH {follower}, {followed} CREATE (follower)-[:`{followup_data}`]->(followed)"
        return self.query_graph(query)


    def delete_node(self, primary_key: str):
        query = f"MATCH (user:User) WHERE user.pk = '{primary_key}' DELETE user"
        return self.query_graph(query)


    def delete_edge(self, node1_primary_key: str, node2_primary_key: str):
        query = "MATCH (:User {pk: '%(user_nd1)s'})<-[f:Follows]->(:User {pk: '%(user_nd2)s'}) DELETE f" % {'user_nd1': node1_primary_key, 'user_nd2': node2_primary_key}
        return self.query_graph(query)


    def query_graph(self, query: str):
        return self.graph.query(query).result_set
