class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:   # if list is empty
            self.head = node
        else:
            current = self.head
            while current.next:     # to last where there is no next
                current = current.next
            current.next = node     # adds to last nodes next

    def display(self):
        values = []
        current = self.head
        while current:     # while there is a node in list
            values.append(current.data[0])     # add value/data to values list
            current = current.next
        return values
