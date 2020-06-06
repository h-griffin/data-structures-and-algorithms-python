class Node():
    def __init__(self, value, next_=None):
            self.value = value
            self.next = next_

    def __repr__(self):
        return f"{self.value} : {self.next}"

class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"linked list : {self.head}"

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += f"{{ {str(current.value)} }} -> "
            current = current.next
        return res + "NULL"

    def insert(self, value):
        """creates Node and adds to head of linked list"""
        self.head = Node(value, self.head)

    def includes(self, value):
        """Bool if value exists as Node value in list"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next #if current is not the value look next
        return False

    def append(self, value):
        """adds new Node to tail of list"""
        current = self.head
        while current:
            if current.next == None: #if there is no next it is the tail
                current.next = Node(value)
                break
            current = current.next

    def insert_before(self, value, newVal):
        """takes in a value already in linked list and a new value to add in place before it"""
        current = self.head
        while current:
            if current.next == None:
                return 'Value not in linked list'
            if current.next.value == value: #create in this spot if the next one is the given value
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def insert_after(self, value, newVal):
        """takes in a value already in linked list and a new value to add after it"""
        current = self.head
        while current:
            if current.next == None:
                return 'Value not in linked list'
            if current.value == value:
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def kth_from_end(self, k):
        """takes in a value(k) and returns the Node k places away from the tail"""
        current = self.head
        arr = []
        if k < 0:
            raise ValueError("value must be positive")
        while current:
            arr.append(current)
            current = current.next

        if len(arr) < k:
            raise IndexError("Value extends length of List.")

        arr.reverse()

        if k == len(arr):
            k = k - 1
        return arr[k].value

class Queue:
    def __init__(self):
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
            raise Exception('cannot dequeue an empty stack')

        exiting = self._front
        self._front = self._front.next
        return exiting.value

    def peek(self):
        """returns front Node vlaue, first in line"""
        if not self._front:
            raise Exception('cannot peek an empty stack')

        return self._front.value

    def is_empty(self):
        """returns bool if queue is empty"""
        #return self.front == None
        return not self._front #front true, not changes to false

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
           self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """removes node on top of stack and returns that value"""
        if not self.top:
            raise Exception('cannot pop an empty stack')

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

#adding some coments to try and save file
