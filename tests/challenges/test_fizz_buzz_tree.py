from dsa.challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinaryTree, BinarySearchTree, Queue, fizz_buzz_tree
import pytest



def test_BinaryTree_breadth():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    actual = tree.breadth_first()
    expected = [1, 5, 4, 7]
    assert actual == expected

def test_BinaryTree_post():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    actual = tree.post_order()
    expected = [7, 5, 4, 1]
    assert actual == expected

def test_fizz_buzz_tree():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ['1', 'Buzz', '4', '7']
    assert actual == expected

def test_fizz_buzz_tree_breadth():
    tree = BinaryTree()
    tree.add(3)
    tree.add(15)
    tree.add(7)
    tree.add(5)
    tree.add(3)
    tree.add(5)
    tree.add(15)
    actual = tree.breadth_first()
    expected = [3, 15, 7, 5, 3, 5, 15]
    assert actual == expected

def test_fizz_buzz_tree_2():
    tree = BinaryTree()
    tree.add(3)
    tree.add(15)
    tree.add(7)
    tree.add(5)
    tree.add(3)
    tree.add(5)
    tree.add(15)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ['Fizz', 'FizzBuzz', '7', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz']
    assert actual == expected
