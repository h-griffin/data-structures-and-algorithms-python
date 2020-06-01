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
        def walk(node): #root of own tree
            """navigates tree"""
            if not node: #base case
                return
            output.append(node.value)
            walk(node.left) # check left
            walk(node.right) # check right
        walk(self.root)
        print(output)
        return output

    def breadth_first(self):
        items = []
        breadth = Queue()
        # add root to queue check empty
        breadth.enqueue(self.root)

        # while someonthing in queue
        while not breadth.is_empty():
            #dequeue
            front = breadth.dequeue()
            #check dequeued left and enqueue if exists
            if front.left:
                breadth.enqueue(front.left)
            #check dequeued right and enqueue if exists
            if front.right:
                breadth.enqueue(front.right)
            #when out of loop done
        return

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
        if not self.root:
            self.root = new_node
            return

        walk_add(self.root, new_node)
        #if value < root -left
        #if value > root -right

    def contains(self, value):
        """takes in a value, returns boolean if value is in tree"""
        pass
        #if value < root -left
        #if value > root -right
        #if value

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

#last line
