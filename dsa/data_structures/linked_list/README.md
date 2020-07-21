# Challenge Summary
linked list

## Challenge Description
create a linked list with nodes linking to eachother

Create a function that returns the node value k places away from teh end/tail

## Approach & Efficiency
 Create a node class with current  and next value properties
Create a linked list class with a head property to identify the first/newest node
Create a function that inserts new nodes to the head of the list
Create a function that checks if a node is already inside the list
	Set the current value to current and while there is a current
	Check if the searchd value is current if not current is next
	Return false if current is never the value
Create a function to add a node to the tail of hte list
	Check for current.next if there is no next it is last
	Set new node as current.nex tto be the new tail
Create a function to insert a new node before a given node
	Check if current.next is the searched value
	Create teh node wile current next is the searched value, playing it before it
Create a function to insert a new node after a given node
If current value is the searched value then next is new val

Create a function that returns the node value k places away from the end/tail
	Create empty array
	If k is less than 0 error, must be positive
	While there is a current value, append to array, then next
		This creates an array with the linked list in order
	Reverse the array
		If the array is the same length as k return k-1 because array indexes at 0
	Return array[k]
the array is in order of the node connections and is reversed



## Solution
![linked list whiteboard image](/assets/linked_list.png)

![ll kth from end whiteboard image](/assets/ll_kth_from_end.png)

## help from :
- Joseph Z
- James S

### Features
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
Ensure your tests are passing before you submit your solution.

Stretch Goal
Create a new branch called doubly-linked-list, and, using the resources available to you online, implement a doubly linked list (completely separate from your singly linked list).

Documentation: Your README.md
# Singly Linked List
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available to your Linked List -->

# Linked list insertions.

### Feature Tasks
Write the following methods for the Linked List class:

.append(value) which adds a new node with the given value to the end of the list
.insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
.insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
Examples
.append(value)
Input	Args	Output
head -> [1] -> [3] -> [2] -> X	5	head -> [1] -> [3] -> [2] -> [5] -> X
head -> X	1	head -> [1] -> X
.insertBefore(value, newVal)
Input	Args	Output
head -> [1] -> [3] -> [2] -> X	3, 5	head -> [1] -> [5] -> [3] -> [2] -> X
head -> [1] -> [3] -> [2] -> X	1, 5	head -> [5] -> [1] -> [3] -> [2] -> X
head -> [1] -> [2] -> [2] -> X	2, 5	head -> [1] -> [5] -> [2] -> [2] -> X
head -> [1] -> [3] -> [2] -> X	4, 5	Exception
.insertAfter(value, newVal)
Input	Args	Output
head -> [1] -> [3] -> [2] -> X	3, 5	head -> [1] -> [3] -> [5] -> [2] -> X
head -> [1] -> [3] -> [2] -> X	2, 5	head -> [1] -> [3] -> [2] -> [5] -> X
head -> [1] -> [2] -> [2] -> X	2, 5	head -> [1] -> [2] -> [5] -> [2] -> X
head -> [1] -> [3] -> [2] -> X	4, 5	Exception
Unit Tests
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

You have access to the Node class and all the properties on the Linked List class.

Write tests to prove the following functionality:

Can successfully add a node to the end of the linked list
Can successfully add multiple nodes to the end of a linked list
Can successfully insert a node before a node located i the middle of a linked list
Can successfully insert a node before the first node of a linked list
Can successfully insert after a node in the middle of the linked list
Can successfully insert a node after the last node of the linked list
Unit tests must be passing before you submit your final solution code.

Stretch Goal
Once you’ve achieved a working solution, write an additional method to delete a node with the given value from the linked list.

Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)

# ll kth from end

### Feature Tasks
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
Example
ll.kthFromEnd(k)
Input ll	Arg k	Output
head -> [1] -> [3] -> [8] -> [2] -> X	0	2
head -> [1] -> [3] -> [8] -> [2] -> X	2	3
head -> [1] -> [3] -> [8] -> [2] -> X	6	Exception
Unit Tests
Where k is greater than the length of the linked list
Where k and the length of the list are the same
Where k is not a positive integer
Where the linked list is of a size 1
“Happy Path” where k is not at the end, but somewhere in the middle of the linked list
Unit tests must be passing before you submit your final solution code.

Stretch Goal
Once you’ve achieved a working solution, implement a method that finds the node at the middle of the Linked List.

Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)
