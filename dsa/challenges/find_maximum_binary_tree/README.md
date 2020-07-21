# Challenge Summary
find maximum binary tree (value)

## Challenge Description
Create  function that takes in a binary tree and returns the highest Node Value

## Approach & Efficiency
Define a function that takes in a tree
Traverse through the tree returning a list of Node values
Set a max value to negative infinity to catch negative values
Iterate through the list of tree values
	If the current value is greater than max value
		Set max value to current value
Return max value

## Solution
![ maximum binary tree whiteboard image](/assets/find_maximum_binary_tree.png)

### Feature Tasks
Write an instance method called find-maximum-value. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
Example
Input
example
![binary tree](assets/binary_tree.png)
Output
11
Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)
