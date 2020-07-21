# Challenge Summary
breadth first binary tree traversal
## Challenge Description
Create a function that takes in a binary tree and traverses through breadth first

## Approach & Efficiency
Create a function that takes in a binary tree
	Create an empty list to hold output
	Create a queue
	Enqueue root
	While there is something in the queue
		Dequeue front / first in line
		Append it to list
		If it has a left or right
			Enqueue left and/or right
	Return output list


## Solution
![ breadth first tree whiteboard image](/assets/breadth_first_tree.png)


### Feature Tasks
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

Example
Input
example
![binary tree](assets/binary_tree.png)
Output
[2,7,5,2,6,9,5,11,4]

Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)
