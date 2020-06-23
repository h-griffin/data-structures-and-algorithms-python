from .linked_list import LinkedList

class Hashmap:
    """
    
    """

    def __init(self, size):
        self.size = size
        self.map = [none] * self.size

    def hash(self, key):
        """takes in a string and returns a hash code"""
        total = 0
        for char in key:
            total += ord(char)

        total *= 19
        hashed_key = total % self.size
        return hashed_key

    def add(self, key, value):
        """takes in key:value pair and adds to hashmap datastructure"""
        hashed_key = self.hash(key)

        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()

        self.map[hashed_key].add([key, value])

    def get(self, key):
        """takes in a key and returns that keys value in the hashmap"""
        index = self.hash(key)

        if self.map[index]:
            ll = self.map[index]
            while ll.head:
                if ll.head.data[0] == key:
                    return ll.head.next
                else:
                    ll.head = ll.head.next
        else:
            return None

def contains(self, key):
    """takes in a key adn returns bool if key exists in hashmap"""
    index = self.hash(key)

    if self.map[index]:
        collection = self.map[index].display()
        if key in collection:
            return True
        else:
            pass
    return False



