import pytest
from dao.graph_dao import GraphDAO

@pytest.mark.asyncio
async def test_graph_dao_get_nodes():
    """ 
    """
    nodes_arr = GraphDAO().get_nodes()
    assert nodes_arr is not None

@pytest.mark.asyncio
async def test_graph_dao_get_nodes():
    graph = await GraphDAO().get_graph()
    assert graph is not None

@pytest.mark.asyncio
async def test_graph_dao_get_neighbours():
    node_id = "sample"
    nodes_arr = await GraphDAO().get_node_neighbours(node_id)
    assert nodes_arr is not None
