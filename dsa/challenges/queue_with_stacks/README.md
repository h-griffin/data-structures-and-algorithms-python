# Challenge Summary
queue with stacks

## Challenge Description
Use two stacks to create a queue that adds nodes to top of stack and removes nodes from the bottom stack

## Approach & Efficiency
Create a stack for inbox, or a main queue
Create a stack for outbox, or a moving temporary queue
Create an enqueue function that adds Nodes to the inbox stack
Create a dequeue function that moves all of inbox to outbox to pop from inbox, then move back
	While inbox is not empty push to outbox
	Once all have been moved to outbox, pop top of stack
		The list has been reversed and now the bottom of inbox is the top of outbox
	After value has popped, enqueue back to inbox, reserving the order of the stack


## Solution
![queue with stacks whiteboard solution](/assets/queue_with_stacks.png)

## help from :
- joseph z
- james s

### Feature Tasks
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

Example

```enqueue(value)
Input	Args	Output
[10]->[15]->[20]	5	[5]->[10]->[15]->[20]
 	5	[5]
dequeue()
Input	Output	Internal State
[5]->[10]->[15]->[20]	20	[5]->[10]->[15])
[5]->[10]->[15]	15	[5]->[10]
```
Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)
