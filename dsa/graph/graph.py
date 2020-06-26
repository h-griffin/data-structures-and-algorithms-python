


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


    def get_vertices(self):
        """returns all keys in graph"""
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex): # get edges
        return self._adjacency_list.get(vertex, [])




class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


