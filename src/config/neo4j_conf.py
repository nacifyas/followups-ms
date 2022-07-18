import neomodel, neomodel.config as config
from models import graph_model

HOST = "atomflare.af"
PORT = 7687
USER = "neo4j"
SECRET = "secret"


def init_db():
    config.DATABASE_URL = f"neo4j://{USER}:{SECRET}@{HOST}:{PORT}"
    neomodel.core.install_all_labels()
