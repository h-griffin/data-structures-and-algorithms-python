import pytest
from dsa.challenges.tree_breadth_first.tree_breadth_first import BinaryTree, Queue, Node, BinarySearchTree

def test_breadth_first():
    bst = BinaryTree()
    bst.add(1)
    bst.add(2)
    bst.add(3)
    bst.add(4)
    bst.add(5)
    actual = bst.breadth_first
    expected = []


def test_pre():
    bst = BinarySearchTree()
    bst.add(1)
    bst.add(2)
    bst.add(3)
    bst.add(4)
    bst.add(5)
    actual = bst.pre_order()
    expected = [1, 2, 3, 4, 5]
    assert actual == expected

def test_in():
    bst = BinarySearchTree()
    bst.add(85)
    bst.add(70)
    bst.add(75)
    bst.add(45)
    bst.add(100)
    bst.add(90)
    bst.add(110)
    actual = bst.in_order()
    expected = [45, 70, 75, 85, 90, 100, 110]
    assert actual == expected

def test_post():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(60)
    bst.add(55)
    bst.add(40)
    bst.add(45)
    actual = bst.post_order()
    expected = [45, 40, 55, 60, 50]
    assert actual == expected

