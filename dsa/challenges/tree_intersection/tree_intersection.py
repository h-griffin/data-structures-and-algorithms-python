from dsa.challenges.breadth_first_tree.breadth_first_tree import Node, BinaryTree, BinarySearchTree, Queue



def tree_intersection(tree1, tree2):
    """takes in two binary trees and returns set of values found in both trees"""
    first_tree = tree1.pre_order()
    second_tree = tree2.pre_order()
    matching = []

    for val in second_tree:
        if val in first_tree:
            matching.append(val)
    return matching




