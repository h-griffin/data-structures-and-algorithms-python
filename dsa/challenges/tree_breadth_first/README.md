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
![ breadth first whiteboard image](/assets/tree_breadth_first.png)
