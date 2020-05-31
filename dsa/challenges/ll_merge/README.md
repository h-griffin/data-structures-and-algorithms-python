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
