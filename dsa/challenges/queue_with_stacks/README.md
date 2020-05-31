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
