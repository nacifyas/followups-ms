from datetime import datetime
from redis.commands.graph.edge import Edge

class FollowUp:
    date_time: datetime = datetime.now()
    label: str = "Follows"

    def create_edge(self, node_follower, node_followed) -> Edge:
        properties = dict(self)
        return Edge(node_follower, self.label, node_followed, properties=properties)
