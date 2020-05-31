class PseudoQueue:
    def __init__(self):
        self._inbox = Stack()
        self._outbox = Stack()


    def enqueue(self, value):
        """takes in a value and adds new node to bottom of stack //add last in line """
        while not self._outbox.is_empty():
            self._inbox.push(self._outbox.pop())
        self._inbox.push(value)


    def dequeue(self):
        """move all item from inbox to outbox then pop from outbox //remove first in line"""
        while not self._inbox.is_empty():
            self._outbox.push(self._inbox.pop())
            # item = self._inbox.pop()
            # self._outbox.push(item)

        if self._outbox.is_empty():
            raise RuntimeError('cannot deque from empty stack')

        outgoing = self._outbox.pop()

        return outgoing


class Node :
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        res = ""
        current = self.top
        while current:
            res += f"{ [current.value]} -> "
            current = current.next
        return res + "NULL"

    def push (self, value):
        """takes in one value and adds new Node to stack"""
        if self.top == None:
            Node(value, self.top)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """removes node on top of stack and returns that value"""
        if self.top:
            outgoing = self.top
            self.top = self.top.next
            return outgoing.value

    def peek(self):
        """returns value of node on top of stack """
        return self.top.value

    def is_empty(self):
        """bool if stack is empty or not"""
        return self.top is None

# E       AssertionError: assert 'NULL' == '[bananas] ->...ples] -> NULL'
# E         - [bananas] -> [apples] -> NULL
# E         + NULL

#like a deck of cards have two stacks
# and move the top half of one stack to
# the other so that the card on the
# bottom of the stack can come out /pop
