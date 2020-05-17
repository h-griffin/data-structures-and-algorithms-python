import pytest
from dsa.challenges.linked_list.linked_list import Linked_list, Node


def test_instance():
    ll = Linked_list()
    assert ll.head == None


def test_insert_empty():
    ll = Linked_list
    ll.insert("apples")
    assert ll.head.value == "apples"


def test_insert_full():
    ll = Linked_list()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"


def test_str():
    ll = Linked_list()
    ll.insert("apples")
    ll.insert("bananas")
    assert str(ll) == "{ bananas } -> { apples } -> NULL"


def tests_node_exception():
    with pytest.raises(TypeError):
        Node("ugh", "this is not a Node")
