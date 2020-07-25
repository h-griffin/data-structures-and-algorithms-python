from .linked_list import LinkedList, Node

class Hashmap:
    """

    """

    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def hash(self, key):
        """takes in a string and returns a hash code"""
        total = 0
        for char in key:                # splitting key
            total += ord(char)          # convert to ascii values
                                        # adding together in total
        total *= 19                     # multiply by -any- prime number
        hashed_key = total % self.size  # modulus by size of hashmap for valid index
        return hashed_key               # store key in valid index

    def add(self, key, value):
        """takes in key:value pair and adds to hashmap datastructure"""
        hashed_key = self.hash(key)

        if not self.map[hashed_key]:                # if there is no duplicate key
            self.map[hashed_key] = LinkedList()     # create linked list for future douplicate keys

        self.map[hashed_key].add([key, value])      # if douplicate exists, add it to linked list

    def get(self, key):
        """takes in a key and returns that keys value in the hashmap"""
        index = self.hash(key)

        if self.map[index]:
            ll = self.map[index]            # index keys are stored in linked list for collisions
            while ll.head:
                if ll.head.data[0] == key:  # if key: is correct
                    return ll.head.data[1]     # return :value
                else:
                    ll.head = ll.head.next  # else look at next key:
        else:
            return None

    def contains(self, key):
        """takes in a key adn returns bool if key exists in hashmap"""
        index = self.hash(key)

        if self.map[index]:
            collection = self.map[index].display()
            if key in collection:
                return True     # will return true only if it can reach it
            else:
                pass
        return False           # if it cant reach it will finish with false after loop



