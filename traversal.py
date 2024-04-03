from collections import deque
from graph import *

def breadth_first(graph, start=0):
    queue = deque()
    queue.append(start)

    visited = np.zeros(graph.numVertices)

    while queue:
        vertex = queue.popleft()

        if visited[vertex] == 1:
            continue

        print("Visit: ", vertex)

        visited[vertex] = 1 # indicate

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.append(v)


g = AdjacencySetGraph(9, directed=True)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

breadth_first(g, 0)