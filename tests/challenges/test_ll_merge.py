from dsa.data_structures.linked_list.linked_list import Node, Linked_list
from dsa.challenges.ll_merge.ll_merge import merge_lists

def test_merge_list_list1_none():
    list1 = Linked_list()
    list2 = Linked_list()
    list2.insert("carrot")
    list2.insert("banana")
    list2.insert("apple")
    actual = str(merge_lists(list1, list2))
    expected = "{ apple } -> { banana } -> { carrot } -> NULL"
    assert actual == expected


def test_merge_list_list2_none():
    list1 = Linked_list()
    list2 = Linked_list()
    list1.insert("carrot")
    list1.insert("banana")
    list1.insert("apple")
    actual = str(merge_lists(list1, list2))
    expected = "{ apple } -> { banana } -> { carrot } -> NULL"
    assert actual == expected

def test_merge_list_equal_lists():
    # list1 = Linked_list()
    # list2 = Linked_list()
    # list1.insert("e")
    # list1.insert("c")
    # list1.insert("a")
    # list2.insert("f")
    # list2.insert("d")
    # list2.insert("b")
    # actual = str(merge_lists(list1, list2))
    # expected = "{ a } -> { b } -> { c } -> { d } -> { e } -> { f } -> NULL"
    # assert actual == expected
    pass


# def test_merge_list_list1_shorter():
#     list1 = Linked_list()
#     list2 = Linked_list()
#     list1.insert("3")
#     list1.insert("1")
#     list2.insert("4")
#     list2.insert("9")
#     list2.insert("5")
#     actual = str(merge_lists(list1, list2))
#     expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL"
#     assert actual == expected


# def test_merge_list_list1_longer():
#     list1 = Linked_list()
#     list2 = Linked_list()
#     list1.insert("3")
#     list1.insert("1")
#     list1.insert("4")
#     list2.insert("9")
#     list2.insert("5")
#     actual = str(merge_lists(list1, list2))
#     expected = "{ 4 } -> { 5 } -> { 1 } -> { 9 } -> { 3 } -> NULL"
#     assert actual == expected
