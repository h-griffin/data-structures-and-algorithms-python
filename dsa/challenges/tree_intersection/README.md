# problem domain
write a function that takes in two binary trees and returns
a set of values
found in both trees.

# edge cases
even / odd length trees

# big O

# algorithm
take in two binary trees
traverse through the first tree returning list of values breadth first
traverse through second tree checking if value is in list
save matching values to new list
return matching values list


# visual
       1            4
     2    3       3   5
   4   5        2  1

Preorder (Root, Left, Right) : 1 2 4 5 3

preorder : 1 2 3 4 5
preorder : 4 3 2 1 5
matching = []

for each value in second tree
    check first tree
        add to list if same

![tree_intersection](assets/tree_intersection.png)

### Feature Tasks
Write a function called tree_intersection that takes two binary tree parameters.
Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write at least three test assertions for each method that you define.

Ensure your tests are passing before you submit your solution.

Example
Input:
![BinaryTree1](assets/BT1.png)
![BinaryTree2](assets/BT2.png)

Output [100,160,125,175,200,350,500]

Stretch Goals
Presume you are working with BSTs. How can you improve the performance of your algorithm?

Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)

