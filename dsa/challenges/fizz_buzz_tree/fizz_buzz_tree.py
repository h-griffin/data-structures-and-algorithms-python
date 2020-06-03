from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node : {self.value}'

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """returns array of values ordered root, left, right"""
        output = []
        def walk(root): #node = root of own tree
            """navigates tree"""
            if not root: #base case
                return
            output.append(root.value)
            walk(root.left) # check left
            walk(root.right) # check right
        walk(self.root)
        # print(output)
        return output

    def breadth_first(self):
        """returns list of Node values breadth first, from tree top to bottom left to right"""
        items = []
        breadth = Queue()
        # add root to queue check empty
        breadth.enqueue(self.root)

        # while someonthing in queue
        while not breadth.is_empty():
            #dequeue
            front = breadth.dequeue()
            items.append(front.value)
            #check dequeued left and enqueue if exists
            if front.left:
                breadth.enqueue(front.left)
            #check dequeued right and enqueue if exists
            if front.right:
                breadth.enqueue(front.right)
            #when out of loop done
        return items

    def add(self, value):
        node = Node(value)
        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            if not front.right:
                front.right = node
                return
            if front.left:
                breadth.enqueue(front.left)
            if front.right:
                breadth.enqueue(front.right)
        return



class BinarySearchTree(BinaryTree):
    #values greater than root go right, less go left

    # def __init__(self):
    #     pass

    def add(self, value):
        """takes in a value, adds a new Node with that value to the correct location in binary search tree"""
        new_node = Node(value) #value from init

        if not self.root:
            self.root = new_node
            return
        def walk_add(node, new):
            """navigates tree and adds new Node"""
            if not node:
                return
            if new_node.value < node.value: #go left
                if not node.left:
                    node.left = new_node
                else:
                    walk_add(node.left, new_node)
            else: #go right
                if not node.right:
                    node.right = new_node
                else:
                    walk_add(node.right, new_node)

        walk_add(self.root, new_node)
        #if value < root -left
        #if value > root -right

    def contains(self, value):
        """takes in a value, returns boolean if value is in tree"""
        if value in self.pre_order(): #collection = []
            return True
        else:
            return False

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """takes in a value and adds it to the left of the root // end of line"""
        self.storage.appendleft(value)

    def dequeue(self):
        """removes Node from the front of queue // first in line"""
        return self.storage.pop()

    def peek(self):
        """returns value of Node at the front of queue // first in line"""
        return self.storage[-1]

    def is_empty(self):
        """returns bool if queue is empty"""
        return len(self.storage) == 0

def fizz_buzz_tree(tree):
    """Takes in a tree as a single argument. Changes values throughout the tree based on Fizzbuzz logic, and returns a new tree in the same order and structure.
    """
    collection = tree.breadth_first()
    new_collection = []

    for i in collection:
        if i % 3 == 0 and i % 5 == 0:
            i = 'FizzBuzz'
            new_collection.append(i)
        elif i % 3 == 0:
            i = 'Fizz'
            new_collection.append(i)
        elif i % 5 == 0:
            i = 'Buzz'
            new_collection.append(i)
        else:
            i = str(i)
            new_collection.append(i)

    new_tree = BinaryTree()

    for i in new_collection:
        new_tree.add(i)

    return new_tree


#last line
