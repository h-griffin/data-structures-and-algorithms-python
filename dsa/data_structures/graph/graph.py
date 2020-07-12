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

    #   add neighbor
    def add_edge(self, start_vertex, end_vertex, weight=0):
        """takes in two vertexes already existing in the graph, with an optional weight. returns nothing"""
        if start_vertex not in self._adjacency_list:
            raise KeyError('start vertex not in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('end vertex not in graph')


        edge = Edge(end_vertex, weight)

        adjacencies = self._adjacency_list[start_vertex] # list of neighbors
        adjacencies.append(edge)

    #   get node
    def get_vertex(self):
        """returns all keys in graph"""
        return self._adjacency_list.keys()

    # def get_neighbors(self, vertex):
    #     """returns all edges"""
    #     return self._adjacency_list.get(vertex, [])       # <<<<<<

    #   get edge   + weight
    def get_neighbors(self, vertex):
        """ Takes in a vertex/node and returns a collection of edges connected to the given vertex/node as well as the weight of the connection.
        """
        collection = []
        connections =  self._adjacency_list.get(vertex, [])         # <<<<<

        for neighbor in connections:
            holder = {}
            holder[neighbor] = neighbor.weight
            collection.append(holder)

        return collection

    def size(self):
        """ Returns the total number of vertices/nodes in the graph"""
        return len(self.graph) if len(self.graph) > 0 else None


    def breadth_first(self, vertex):
        """ Takes in a node/vertex and performs a breadth first traversal of the graph. This will return a collection of the nodes/vertices within the graph from a breadth first traversal perspective of the given node/vertex.
        """
        nodes = []
        holder = set()
        breadth = Queue()
        holder.add(vertex.value)
        breadth.enqueue(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self.graph[front]:
                if child.vertex.value not in holder:
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes
