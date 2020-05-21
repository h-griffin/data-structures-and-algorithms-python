class Linked_list:
    def __init__(self, value=None):
        self.head = None

    def __repr__(self):
        return f"linked list : {self.head}"

    def __str__(self):
        answer = ""
        current = self.head

        while current:
            # { bananas } -> { apples } -> NULL
            answer += f"{{ {str(current.value)} }} -> "
            current = current.next

            return answer + "NULL"

    def insert(self, value):
        """creates new Node and adds to linked-list"""
        self.head = Node(value, self.head)

    def includes(self, value):
        """boolean t/f if value exists as Node in list"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        # adds new node to end of list
        pass

    def insert_after(self, value, newVal):
        # insert newVal node immediatly after first value node
        pass


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



