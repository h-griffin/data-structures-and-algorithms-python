# Challenge Summary
binary search tree

## Challenge Description
Create binary search tree class that takes in a binary tree and traverses depth first

## Approach & Efficiency
Create a binary tree class (this will be the super class of BST)
Create a method for traversal
	Create an empty variable for the output , a list
	Create a method called walk that will traverse through the tree (pre order below)
		Append the node value  (root that called walk)
		Call the walk method again for the left value
		Call the walk method again for the right value
	Call the walk metod with the root
Return the output
Create a binary search tree class that inherits the binary tree clas
Create a function to add values to the tree
	Define a walk method that takes in a node to find and a new node to add
		If the new node is greater than the root go left
			If there is no left add to left
			If there is a left, walk left and to the lefts left
		Else go right
			If there is no right add to right
			If there is right, walk right adn add to rights right
		If there is no root (empty tree)
			Set new node to root
Define a contains method that takes in a value and searches the tree
	Run thte tree though a traversal method returning a list of values
		Iterate through list and return true or false

## Solution
![ binary search tree whiteboard image](/assets/tree.png)

### Features
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Create a BinaryTree class
- Define a method for each of the depth first traversals called **preOrder**, **inOrder**, and **postOrder** which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
- Create a BinarySearchTree class
- Define a method named **add** that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- Define a method named **contains** that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

Can successfully instantiate an empty tree
Can successfully instantiate a tree with a single root node
Can successfully add a left child and right child to a single root node
Can successfully return a collection from a preorder traversal
Can successfully return a collection from an inorder traversal
Can successfully return a collection from a postorder traversal
Ensure your tests are passing before you submit your solution.

Stretch Goal
Create a new branch called k-ary-tree, and, using the resources available to you online, implement a k-ary tree, where each node can have any number of children.

