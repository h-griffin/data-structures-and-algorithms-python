from dsa.graph.graph import Graph, Vertex, Edge

def get_edges(graph, alist):
    global weight
    global start
    global end

    status = True
    weight = 0
    start = 0
    end = 1

    def travel(graph, start, end):
        route = graph.graph[start]

        for city in route:

            if end == city.vertex:
                global weight
                weight += city.weight

                if end.value == alist[-1].value:
                    break
                else:
                    global start
                    start += 1
                    global end
                    end += 1
                    travel(graph, alist[start], alist[end])

    travel(graph, alist[start], alist[end])

    if weight == 0:
        status = False

    weight = f"${str(weight)}"
    return (status, weight,)
