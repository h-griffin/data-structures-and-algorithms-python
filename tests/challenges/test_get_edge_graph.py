import pytest

from dsa.challenges.get_edge_graph.get_edge_graph import Graph, Vertex

# vertex = node
def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('spam')
    actual = vertex.value
    expected = 'spam'
    assert actual == expected

def test_add_edge():
    graph = Graph()

    apples = graph.add_vertex('apples')
    bananas = graph.add_vertex('bananas')
    graph.add_edge(apples, bananas)

    assert True, ('will be fully excersized in get neighbors test')

def test_add_edge_outsider():
    """edge can only be created between two vertexes inside graph"""
    graph = Graph()
    insider = graph.add_vertex('insider')
    outsider = Vertex('outsider')

    with pytest.raises(KeyError):
        graph.add_edge(outsider, insider )


def test_get_vertices():
    # returns collection of all vertices
    graph = Graph()
    apples = graph.add_vertex('apples')
    bananas = graph.add_vertex('bananas')

    actual = graph.get_vertex()
    assert len(actual) == 2


# def test_get_edges(): # edges = neighbors
#     graph = Graph()
#     apples = graph.add_vertex('apples')
#     bananas = graph.add_vertex('bananas')
#     graph.add_edge(apples, bananas)
#     neighbors = graph.get_neighbors(apples)
#     assert len(neighbors) == 1
#     neighbor = neighbors[0]
#     assert neighbors[0].vertex.value == 'bananas'     <<<<<
#     assert neighbor.weight == 0

def test_get_size():
    """test number of vertexes"""
    graph = Graph()
    apples = graph.add_vertex('apples')
    bananas = graph.add_vertex('bananas')

    assert len(graph) == 2

def test_get_neighbors_none():
    g = Graph()
    node_a = g.add_vertex('a')
    node_b = g.add_vertex('b')
    node_c = g.add_vertex('c')
    node_d = g.add_vertex('d')
    actual = g.get_neighbors(node_a)
    expected = []
    assert actual == expected

def test_get_neighbors_1():
    g = Graph()
    node_a = g.add_vertex('a')
    node_b = g.add_vertex('b')
    node_c = g.add_vertex('c')
    node_d = g.add_vertex('d')
    g.add_edge(node_a, node_b)
    actual = len(g.get_neighbors(node_a))
    expected = 1
    assert actual == expected
