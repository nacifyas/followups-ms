from config.redis_conf import redis_connection as redis
from models.followup_edge import FollowUp
from models.user_node import User
from redis.commands.graph import Graph


class GraphDAO():
    graph: Graph

    def __init__(self, graph: Graph = redis.graph("users_followups")):
        self.graph = graph


    def get_graph(self, limit: int = 50):
        return self.graph.query("MATCH (m) RETURN m").result_set


    def create_node(self, node: User):
        self.graph.add_node(node.to_node())
        return self.commit_to_graph()


    def create_edge(self, node_follower, node_followed) -> Graph:
        edge = FollowUp().create_edge(node_follower, node_followed)
        return self.graph.add_edge(edge)


    def commit_to_graph(self):
        return self.graph.commit().result_set
