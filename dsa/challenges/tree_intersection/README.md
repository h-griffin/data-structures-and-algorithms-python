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

