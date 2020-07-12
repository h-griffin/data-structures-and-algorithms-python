from dsa.challenges.get_edge_graph.get_edge_graph import get_edges
from dsa.graph.graph import Graph, Vertex, Edge


def test_get_edges():
    g = Graph()
    apple = g.add_vertex('Apple')
    banana = g.add_vertex('Banana')
    carrot = g.add_vertex('Carrot')

    g.add_edge(apple,banana, 10)
    g.add_edge(apple,carrot,20)
    g.add_edge()

