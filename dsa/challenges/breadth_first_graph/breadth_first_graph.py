from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def __len__(self):
        """returns length of key list, which gives number of keys"""
        return len(self._adjacency_list)

    # vertex = node
    def add_vertex(self, value):
        """takes in a value and returns the vertex after it adds it to the graph"""
        v = Vertex(value)
        self._adjacency_list[v] = [] # list of neighbors
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0): # add neighbor
        """takes in two vertexes already existing in the graph, with an optional weight. returns nothing"""
        if start_vertex not in self._adjacency_list:
            raise KeyError('start vertex not in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('end vertex not in graph')


        edge = Edge(end_vertex, weight)

        adjacencies = self._adjacency_list[start_vertex] # list of neighbors
        adjacencies.append(edge)


    def get_vertex(self):
        """returns all keys in graph"""
        return self._adjacency_list.keys()

    def get_edges(self, vertex):
        """returns all edges/ neighbors"""
        return self._adjacency_list.get(vertex, [])

    def size(self):
        """ Returns the total number of vertices/nodes in the graph"""
        return len(self._adjacency_list) if len(self._adjacency_list) > 0 else None

    def breadth_first(self, vertex):
        """ Takes in a node/vertex and returns a breadth first traversal of the graph values"""
        nodes = []
        holder = set()
        breadth = Queue()                  # create Q
        holder.add(vertex.value)           # add value to set
        breadth.enqueue(vertex)            # put the vertex in line to queue its children

        while not breadth.is_empty():      # false
            front = breadth.dequeue()      # remove from queue
            nodes.append(front.value)      # add value to list after removing from queue

            for child in self._adjacency_list[front]:       # queue its children
                if child.vertex.value not in holder:        # unvisited child
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes



class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance."""
        self.storage.appendleft(value)

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue, and returns the node's value."""
        return self.storage.pop()

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        return self.storage[-1]

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return len(self.storage) == 0


