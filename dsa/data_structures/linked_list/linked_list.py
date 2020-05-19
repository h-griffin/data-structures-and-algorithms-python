class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"linked list : {self.head}"

    def __str__(self):
        res = ""
        current = self.head

        while current:
            # { bananas } -> { apples } -> NULL
            res += "{ " + str(current.value) + " } -> "
            current = current.next

            return res + " NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        #if value exists as Node value in list
        pass
    
    def append(self, value):
      #adds new node to end of list
      pass

    def insert_after(self, value, newVal):
      #insert newVal node immediatly after first value node
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
