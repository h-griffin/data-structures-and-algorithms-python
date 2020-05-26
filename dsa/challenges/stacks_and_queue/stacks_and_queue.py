class Node():
    def __init__(self, value, next_=None):
            self.value = value
            self.next = next_

    def push(self):
        pass
    def pop(self):
        pass
    def peek(self):
        pass
    def is_empty(self):
        pass

class Linked_list:
    pass

class Queue:
    def __init__(self):
        self._storage = Linked_list()
        self._front = None
        self._rear = None

    def enqueue(self, value):
        """add new value to front of linked list"""
        node = Node(value)

        if self._rear: #true or false
            self._rear.next = node
            self._rear = node

        else:
            #no one else in line ,new node is front and rear
            self._rear = self._front = node

    def dequeue(self):
        """removes node from linked list"""
        if not self._front:
            raise Exception('cannot peek an empty stack')

        exiting = self._front
        self._front = self._front.next
        return exiting.value

    def peek(self):

        if not self._front:
            raise Exception('cannot peek an empty stack')

        return self._front.value

    def is_empty(self):
        #return self.front == None
        return not self._front #front true, not changes to false

if __name__ == "__main__":
    colors = Queue()
    assert colors.is_empty()

    try:
        assert colors.peek() == None
    except Exception:
        print('good, should be an error here')
    else:
        print('exception should have been thrown')

    colors.enqueue('green')
    assert not colors.is_empty()
    assert colors.peek() == 'green'

    colors.enqueue('pink')
    assert colors.peek() == 'green'
    assert colors._front.value == 'green'
    assert colors._rear.value == 'pink'

    out = colors.dequeue()
    assert out == 'green'

    out = colors.dequeue()
    assert out == "pink"

    assert colors.is_empty

    print('******** all good! ********')
