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
        if k < 0:
            raise ValueError("value must be positive")
        while current:
            if current.next == None:
                return current - k
            else:
                return 'not working'

# not for public use
class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        # dont check node check if it has value and next
        # 'ducktyping'
        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"
