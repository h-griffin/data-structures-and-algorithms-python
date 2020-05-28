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

class AnimalShelter:

    def __init__(self):
        self.kennel = Stack()
        self.temp = []


    def enqueue(self, animal):
        if animal in ['cat','dog']:
            self.kennel.push(animal)
            print(self.kennel)

    def dequeue(self, pref):
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



if __name__ == "__main__":
    # pass

## tests
# def test_empty_kennel():
#     actual = AnimalShelter.kennel.is_empty()
#     expected = None
#     assert actual == expected

# def test_is_peek():
    kennel = AnimalShelter()
    kennel_ref = [kennel.enqueue(i) for i in ['cat', 'dog', 'cat']]
    actual = kennel_ref.kennel.peek()
    assert actual == 'cat'

    actual = kennel_ref.kennel.pop()
    assert actual == 'dog'
    #shfshfd

#changes for commit
 