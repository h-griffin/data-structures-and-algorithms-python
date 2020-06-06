from dsa.challenges.tree.tree import BinaryTree, BinarySearchTree, Node

def test_tree():
    assert BinaryTree()

def test_single_root():
    bst = BinarySearchTree()
    bst.add(1)
    actual = bst.root.value
    expected = 1
    assert actual == expected


def test_left_right():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(1)
    bst.add(3)
    right = bst.root.right.value
    expected_right = 3
    left = bst.root.left.value
    expected_left = 1
    assert right == expected_right
    assert left == expected_left

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

def test_contains():
    bst = BinarySearchTree()
    bst.add(1)
    bst.add(2)
    bst.add(3)
    actual = bst.contains(2)
    expected = True
    assert actual == expected



