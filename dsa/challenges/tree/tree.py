class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """returns array of values ordered _"""
        output = []
        #depth first // root, all left, then right
        def walk(node):
            if not node:
                return
            output.append(node.value)
            node.pre_order(node.left)
            node.pre_order(node.right)

        walk(self.root)
        return output

    def in_order(self):
        """returns array of values ordered _"""
        pass

    def post_order(self):
        """returns array of values ordered _"""
        pass

class BinarySearchTree(BinaryTree):
    #values greater than root go right, less go left

    # def __init__(self):
    #     pass

    def add(self, value):
        """takes in a value, adds a new Node with that value to the correct location in binary search tree"""
        new_node = Node(value) #value from init
        
        def walk(node, new):
            if new_node.value < node.value:
                if not node.left:
                    node.left = new_node
                else:
                    walk(node.left, new_node)
            else:
                if not node.right:
                    node.right = new_node
                else:
                    walk(node.right, new_node)


        if not self.root:
            self.root = new_node
            return

        walk(self.root, new_node)
        #if value < root -left
        #if value > root -right

    def contains(self, value):
        """takes in a value, returns boolean if value is in tree"""
        pass
        #if value < root -left
        #if value > root -right
        #if value


bst = BinarySearchTree()
bst.add(4)
bst.add(7)
bst.add(5)
bst.add(9)
bst.add(2)
bst.add(30)
bst.add(-1)
bst.pre_order()
#last line
