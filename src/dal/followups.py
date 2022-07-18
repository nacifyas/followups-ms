from lib2to3.pgen2 import driver
from config.neo4j_conf import init_driver

DATABASE = ""

driver = init_driver()

with driver.session(database=DATABASE) as session:
    pass