# Challenge Summary
linked list merge

## Challenge Description
Create a function that takes two linked lists and merges/zipps them together starting with list one then list two

## Approach & Efficiency
Create a function that takes in two lists and merges them together starting with 1 then 2
Create a new list to merge the two
while  list 1 and 2 have a current and lew list has no head/ empty
	Insert then append
		This keeps the order of the lists, insert will create then append will go after
	If current has a next,
Change current to next now that current is in the new list already
When there are no values left, return new list


## Solution
![ll merge whiteboard image](/assets/ll_merge.png)

## help from :
- joseph z

# ll merge
### Zip two linked lists.

Feature Tasks
Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
Example

```zipLists(list1, list2)
Arg list1	Arg list2	Output
head -> [1] -> [3] -> [2] -> X	head -> [5] -> [9] -> [4] -> X	head -> [1] -> [5] -> [3] -> [9] -> [2] -> [4] -> X
head -> [1] -> [3] -> X	head -> [5] -> [9] -> [4] -> X	head -> [1] -> [5] -> [3] -> [9] -> [4] -> X
head -> [1] -> [3] -> [2] -> X	head -> [5] -> [9] -> X	head -> [1] -> [5] -> [3] -> [9] -> [2] -> X
```

Stretch Goal
Once you’ve achieved a working solution, implement another function that merges two sorted linked lists into a single sorted linked list.

Requirements
Ensure your complete solution follows the standard requirements.

Write unit tests
Follow the template for a well-formatted README
Submit the assignment following these instructions
