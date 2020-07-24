class Node :
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push (self, value):
        """takes in a value and adds node-value to top of stack"""
        self.top = Node(value, self.top)

    def pop(self):
        """removes value from top of stack and returns its value"""
        if self.top:
            outgoing = self.top
            self.top = self.top.next
            return outgoing.value

    def peek(self):
        """returns value at top of stack"""
        return self.top.value

    def is_empty(self):
        """boolean if stack is empty"""
        return self.top is None

class AnimalShelter:

    def __init__(self):
        self.kennel = Stack()
        self.temp = []


    def enqueue(self, animal):
        """takes in an animal and adds to queue if it is dog or cat"""
        if animal in ['cat','dog']:
            self.kennel.push(animal)
            print(self.kennel)

    def dequeue(self, pref):
        """takes in a preference and returns dog or cat first in line, if no pref is given, null"""
        if pref in ['cat', 'dog']:
            while self.kennel.peek() != pref:
              self.temp.append(self.kennel.pop())
            popped = self.kennel.pop()
            while self.temp != []:
                self.kennel.push(self.temp[-1])
            print(self.kennel)
            return popped
        if pref not in ['cat', 'dog']:
            return None

