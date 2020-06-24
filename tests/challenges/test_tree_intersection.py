import pytest
from dsa.challenges.breadth_first_tree.breadth_first_tree import BinaryTree, Queue, Node, BinarySearchTree
from dsa.challenges.tree_intersection.tree_intersection import tree_intersection


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

def test_tree_intersection():
    bst1 = BinaryTree()
    bst1.add(1)
    bst1.add(2)
    bst1.add(3)

    bst2 = BinaryTree()
    bst2.add(2)
    bst2.add(3)
    bst2.add(4)

    actual = tree_intersection(bst1, bst2)
    expected = [2, 3]
    assert actual == expected

def test_tree_intersection_odd():
    bst1 = BinaryTree()
    bst1.add(1)
    bst1.add(2)
    bst1.add(3)
    bst1.add(4)

    bst2 = BinaryTree()
    bst2.add(2)
    bst2.add(3)
    bst2.add(4)
    bst2.add(5)
    bst2.add(6)

    actual = tree_intersection(bst1, bst2)
    expected = [2, 3, 4]
    assert actual == expected


def test_tree_intersection_negative():
    bst1 = BinaryTree()
    bst1.add(1)
    bst1.add(-2)
    bst1.add(3)
    bst1.add(4)

    bst2 = BinaryTree()
    bst2.add(1)
    bst2.add(2)
    bst2.add(3)
    bst2.add(-4)

    actual = tree_intersection(bst1, bst2)
    expected = [1, 3]
    assert actual == expected
