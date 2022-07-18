from neo4j import GraphDatabase


HOST = "atomflare.af"
PORT = 7687
USER = "neo4j"
SECRET = "secret"

def init_driver():
    neo4j_url = f"neo4j://{HOST}:{PORT}"

    driver = GraphDatabase.driver(
        neo4j_url,
        auth=(USER, SECRET)
        )

    driver.verify_connectivity()

    return driver