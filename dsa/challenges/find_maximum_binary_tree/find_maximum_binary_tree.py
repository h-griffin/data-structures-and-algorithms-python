from collections import deque
from dsa.challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinarySearchTree, BinaryTree, Queue


def find_maximum_value(tree):
    """Takes in a tree as a single argument. returns greatest Node value in tree."""
    collection = tree.breadth_first() #list
    max_val = 0

    for i in collection:
        if i > max_val:
            max_val = i

    return max_val
