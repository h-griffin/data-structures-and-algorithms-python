from dsa.data_structures.linked_list.linked_list import Linked_list, Node
import pytest


def test_instance():
    ll = Linked_list()
    assert ll.head == None


def test_insert_empty():
    ll = Linked_list
    ll.insert("apples", None)
    assert ll.head.value == "apples"


def test_insert():
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

def test_insert_before(llist):
    llist.insert_before("apple", "donut" )
    assert str(llist) == "{ carrot } -> { banana } -> { donut } -> { apple } -> NULL"

def test_insert_after(llist):
    llist.insert.after("banana", "donut")
    assert str(llist) == "{ carrot } -> { banana } -> { donut } -> { apple } -> NULL"


def test_includes_true(llist):
    assert llist.includes("carrot") == True

def test_includes_false(llist):
    assert llist.includes("donut") == False

def test_append(llist):
    llist.append("donut")
    assert str(llist) == "{ carrot } -> { banana } -> { apple } -> { donut } -> NULL"

def test_k():
    ll = Linked_list()
    ll.insert(5)    # 5- 4- 3- 2- 1
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 5
    assert actual == expected

@pytest.fixture
def llist():
    """linked list for testing"""
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("carrot")
    return ll #"{ carrot } -> { banana } -> { apple } -> NULL"
