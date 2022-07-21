from config.redis_conf import redis_connection as redis
from models.followup_edge import FollowUp
from models.user_node import User
from redis.commands.graph import Graph


class GraphDAO():
    graph: Graph

    def __init__(self, graph: Graph = redis.graph("users_followups")):
        self.graph = graph

    def get_node_by_id(self, node_id: str):
        query = ""
        return self.query_graph(query)

    def get_graph(self, limit: int = 50):
        return self.graph.query("MATCH (m) RETURN m").result_set


    def create_node(self, node: User):
        self.graph.add_node(node.to_node())
        return self.commit_to_graph()


    def create_edge(self, node_follower_id: str, node_followed_id: str):
        node_follower = self.get_node_by_id(node_follower_id)
        node_followed = self.get_node_by_id(node_followed_id)
        edge = FollowUp().create_edge(node_follower, node_followed)
        self.graph.add_edge(edge)
        return self.commit_to_graph()


    def delete_node(self, node_id: str):
        query = ""
        return self.query_graph(query)


    def delete_edge(self, edge_id: str):
        query = ""
        return self.query_graph(query)


    def commit_to_graph(self):
        return self.graph.commit().result_set

    def query_graph(self, query: str):
        return self.graph.query(query).result_set
