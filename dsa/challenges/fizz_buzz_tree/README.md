# Challenge Summary
fizz buzz tree

## Challenge Description
Create a function that takes in a tree as an argument and returns a new tree in the same order with values changed according to Fizz Buzz rules

## Approach & Efficiency
Create a function that takes in a tree as an argument and returns a new tree in the same order
Create a function that takes in a tree as an argument
The tree passed in returns a list of the tree values in order
Pass this list into breadth first which goes top to bottom left to right
Create a new list that is empty
Iterate through the original list that was passed in
	If the remainder of the value divided by 3 or 5 equals zero then the value is divisible
    -iterate through, changing values following fizz buzz rules-
	Append these changed values to the new list
Create a new tree
Iterate through the new list with the changed values
	For each value add to new tree


## Solution
![ whiteboard image](/assets/fizz_buzz_tree.png)

## worked with:
- joseph z

### Feature Tasks
Write a function called FizzBuzzTree which takes a k-ary tree as an argument.
Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.
Return a new tree.
Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)
