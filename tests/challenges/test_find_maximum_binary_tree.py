from dsa.challenges.find_maximum_binary_tree.find_maximum_binary_tree import find_maximum_value
from collections import deque
from dsa.challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinarySearchTree, BinaryTree, Queue
import pytest

def test_max_val():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    actual = find_maximum_value(tree)
    expected = 7
    assert actual == expected

def test_max_val_zero():
    tree = BinaryTree()
    tree.add(-1)
    tree.add(-5)
    tree.add(0)
    tree.add(-7)
    actual = find_maximum_value(tree)
    expected = 0
    assert actual == expected

def test_max_val_negative():
    tree = BinaryTree()
    tree.add(-1)
    tree.add(-5)
    tree.add(-4)
    tree.add(-7)
    actual = find_maximum_value(tree)
    expected = -1
    assert actual == expected


