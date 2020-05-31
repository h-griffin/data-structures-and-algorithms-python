import pytest
from dsa.data_structures.linked_list.linked_list import Linked_list

def test_ll_instance():
    assert Linked_list()

def test_ll_str():
    ll = Linked_list
    ll.insert('apple')
    ll.insert('banana')
    actual = str(ll)
    expected = "{ banana } -> { apple } -> NULL"
    assert actual == expected

def test_ll_repr():
    ll = Linked_list()
    actual = repr(ll)
    expect = "linked list : None"
    assert actual == expect
#last line
