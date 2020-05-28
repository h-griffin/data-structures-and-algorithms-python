class PseudoQueue:
    def __init__(self):
        self._inbox = Stack()
        self._outbox = Stack()


    def enqueue(self, value):

        while not self._outbox.is_empty():
            self._inbox.push(self._outbox.pop())
        self._inbox.push(value)


    def dequeue(self):
        """move all item from inbox to outbox then pop from outbox"""
        while not self._inbox.is_empty():
            self._outbox.push(self._inbox.pop())
            # item = self._inbox.pop()
            # self._outbox.push(item)

        if self._outbox.is_empty():
            raise RuntimeError('cannot deque from empty stack')

        outgoing = self._outbox.pop()

        return outgoing


class Node :
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push (self, value):
        self.top = Node(value, self.top)

    def pop(self):

        if self.top:
            outgoing = self.top
            self.top = self.top.next
            return outgoing.value

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.top is None


#like a deck of cards have two stacks
# and move the top half of one stack to
# the other so that the card on the
# bottom of the stack can come out /pop
