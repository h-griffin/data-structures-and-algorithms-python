import pytest
from dsa.data_structures.linked_list.linked_list import Linked_list

def test_ll_instance():
    assert Linked_list()

def test_LinkedList_str():
    """uses insert() to test str()"""
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    actual = str(ll)
    expected = "{ banana } -> { apple } -> NULL"
    assert actual == expected

def test_ll_repr():
    """uses an empty linked list to test repr()"""
    ll = Linked_list()
    actual = repr(ll)
    expect = "linked list : None"
    assert actual == expect

def test_ll_head():
    """uses an empty linked list to test _init_()"""
    ll = Linked_list()
    assert ll.head == None

def test_ll_insert():
    """tests insert() adds node to head"""
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    assert ll.head.value == "banana"
    assert ll.head.next.value == 'apple'

def test_ll_includes_true():
    """uses insert() to test includes()"""
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("carrot")
    actual = ll.includes("carrot")
    expected = True
    assert actual == expected

def test_ll_includes_false():
    """uses insert() to test includes()"""
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("carrot")
    actual = ll.includes("donut")
    expected = False
    assert actual == expected

def test_ll_insert_before(ll_list):
    """uses pytest fixture to test insert_before() adds node before given value"""
    ll_list.insert_before("apple", "donut")
    actual = str(ll_list)
    expected = "{ carrot } -> { banana } -> { donut } -> { apple } -> NULL"
    assert actual == expected

def test_ll_insert_after(ll_list):
    """uses pytest fixture to test insert_after() adds node after given value"""
    ll_list.insert_after("banana", "donut")
    actual = str(ll_list)
    expected = "{ carrot } -> { banana } -> { donut } -> { apple } -> NULL"
    assert actual == expected

def test_ll_append(ll_list):
    """uses pytest fixture to test append() adds node to tail"""
    ll_list.append("donut")
    actual = str(ll_list)
    expected = "{ carrot } -> { banana } -> { apple } -> { donut } -> NULL"
    assert actual == expected

def test_LinkedList_kth_from_end_0():
    """uses insert to test kth_from_end() returns k places away from tail"""
    ll = Linked_list()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 2
    assert actual == expected

def test_LinkedList_kth_from_end_2():
    """uses insert to test kth_from_end() returns k places away from tail"""
    ll = Linked_list()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(2)
    expected = 3
    assert actual == expected


def test_node_exception():
    # with pytest.raises(TypeError):
    #     Node("Test", "This must be a node not a string")
    pass



@pytest.fixture
def ll_list():
    """Sets up a linked list instance along with adds 3 nodes for testing "{ carrot } -> { banana } -> { apple } -> NULL""""
    ll = Linked_list()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("carrot")
    return ll
#last line

