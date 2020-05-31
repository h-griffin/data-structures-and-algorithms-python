# Challenge Summary
linked list

## Challenge Description
create a linked list with nodes linking to eachother

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



## Solution
![linked list whiteboard image](/assets/linked_list.png)

