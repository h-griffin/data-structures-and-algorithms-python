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
