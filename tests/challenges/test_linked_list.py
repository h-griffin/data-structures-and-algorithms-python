import pytest
from dsa.data_structures.linked_list.linked_list import Linked_list

def test_ll_instance():
    assert Linked_list()

def test_LinkedList_str():
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    actual = str(ll)
    expected = "{ banana } -> { apple } -> NULL"
    assert actual == expected

def test_ll_repr():
    ll = Linked_list()
    actual = repr(ll)
    expect = "linked list : None"
    assert actual == expect

def test_ll_head():
    ll = Linked_list()
    assert ll.head == None

def test_ll_insert():
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    assert ll.head.value == "banana"
    assert ll.head.next.value == 'apple'

def test_ll_includes_true():
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("carrot")
    actual = ll.includes("carrot")
    expected = True
    assert actual == expected

def test_ll_includes_false():
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("carrot")
    actual = ll.includes("donut")
    expected = False
    assert actual == expected


def test_node_exception():
    # with pytest.raises(TypeError):
    #     Node("Test", "This must be a node not a string")
    pass

#last line

