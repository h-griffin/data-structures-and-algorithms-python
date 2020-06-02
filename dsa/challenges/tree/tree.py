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
            output.append(node.value) # root
            walk(node.left) # check left
            walk(node.right) # check right
        walk(self.root)
        print(output)
        return output


    def in_order(self):
        """returns array of values ordered left, root, right"""
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) # check left
            output.append(node.value) # root
            walk(node.right) # check right
        walk(self.root)
        return output


    def post_order(self):
        """returns array of values ordered left, right, root"""
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) # check left
            walk(node.right) # check right
            output.append(node.value) # root
        walk(self.root)
        return output


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

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(7)
    bst.add(5)
    bst.add(9)
    bst.add(2)
    bst.add(30)
    bst.add(-1)
    bst.pre_order()


#notes

#        1
#     2    3
#   4   5

# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1

#SyntaxError: unexpected EOF while parsing


