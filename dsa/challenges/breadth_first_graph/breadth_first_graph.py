from collections import deque
from dsa.challenges.stacks_and_queue.stacks_and_queue import Queue
from dsa.graph.graph import Graph, Vertex, Edge


def test_breadth_first_example_2():
    """ Refer to the README Examples for visual aids.
    """
    g = Graph()
    apple = g.add_node('Apple')
    banana = g.add_node('Banana')
    carrot = g.add_node('Carrot')
    egg = g.add_node('Egg')
    donut = g.add_node('Donut')
    g.add_edge(apple, banana)
    g.add_edge(banana, apple)
    g.add_edge(banana, donut)
    g.add_edge(banana, carrot)
    g.add_edge(banana, egg)
    g.add_edge(donut, tom)
    g.add_edge(donut, carrot)
    g.add_edge(carrot, donut)
    g.add_edge(carrot, tom)
    g.add_edge(carrot, egg)
    g.add_edge(egg, sam)
    g.add_edge(egg, tom)
    actual = g.breadth_first(bob)
    expected = ['Apple', 'Banana', 'Donut', 'Carrot', 'Egg']
    assert actual == expected




