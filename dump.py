# from config.redis_conf import redis_connection as redis
# from redis.commands.graph.edge import Edge
# from redis.commands.graph.node import Node
# from datetime import datetime


# # Create a graph
# graph = redis.graph("users_followups")

# # Create a node
# user_node1 = Node(label="User", properties={"name": "Alex", "age": 35})
# user_node2 = Node(label="User", properties={"name": "Carl", "age": 30})


# # Add node to the graph
# graph.add_node(user_node1)
# graph.add_node(user_node2)

# # Define edge
# edge1 = Edge(user_node1, "Follows", user_node2, properties={"data_time": datetime.now()})

# # Add edge to the graph
# graph.add_edge(edge1)

# # Create the graph into the db
# graph.commit()

# CRUD via graph.querry("CYPHER QUERRY LANGUAGE")


from config.redis_conf import redis_connection as r
from redis.commands.graph.edge import Edge
from redis.commands.graph.node import Node

# Connect to a database
# r = redis.Redis(host="<endpoint>", port="<port>", 
#                 password="<password>")

# Create nodes that represent users
users = { "Alex": Node(label="Person", properties={"name": "Alex", "age": 35}),
          "Jun": Node(label="Person", properties={"name": "Jun", "age": 33}),
          "Taylor": Node(label="Person", properties={"name": "Taylor", "age": 28}),
          "Noor": Node(label="Person", properties={"name": "Noor", "age": 41}) }

# Define a graph called SocialMedia
social_graph = r.graph("SocialMedia")

# Add users to the graph as nodes
for key in users.keys():
    social_graph.add_node(users[key])

# Add relationships between user nodes
social_graph.add_edge( Edge(users["Alex"], "friends", users["Jun"]) )
# Make the relationship bidirectional
social_graph.add_edge( Edge(users["Jun"], "friends", users["Alex"]) )

social_graph.add_edge( Edge(users["Jun"], "friends", users["Taylor"]) )
social_graph.add_edge( Edge(users["Taylor"], "friends", users["Jun"]) )

social_graph.add_edge( Edge(users["Jun"], "friends", users["Noor"]) )
social_graph.add_edge( Edge(users["Noor"], "friends", users["Jun"]) )

social_graph.add_edge( Edge(users["Alex"], "friends", users["Noor"]) )
social_graph.add_edge( Edge(users["Noor"], "friends", users["Alex"]) )

# Create the graph in the database
social_graph.commit()

# Query the graph to find out how many friends Alex has
result1 = social_graph.query("MATCH (p1:Person {name: 'Alex'})-[:friends]->(p2:Person) RETURN count(p2)")
print("Alex's original friend count:", result1.result_set)

# Delete a relationship without deleting any user nodes
social_graph.query("MATCH (:Person {name: 'Alex'})<-[f:friends]->(:Person {name: 'Jun'}) DELETE f")

# Query the graph again to see Alex's updated friend count
result2 = social_graph.query("MATCH (p1:Person {name: 'Alex'})-[:friends]->(p2:Person) RETURN count(p2)")
print("Alex's updated friend count:", result2.result_set)

print(social_graph)
# Delete the entire graph
# social_graph.delete()
