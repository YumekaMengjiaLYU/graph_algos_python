from collections import deque
from graph import *

def topological_sort(graph):
    queue = deque()

    indegree_map = {}

    for i in range(graph.numVertices):
        indegree_map[i] = graph.get_indegree(i)

        if indegree_map[i] == 0:
            queue.append(i)

    sorted_list = []
    while queue:
        vertex = queue.popleft()

        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] = indegree_map[v] - 1
            if indegree_map[v] == 0:
                queue.append(v)

    if len(sorted_list) != graph.numVertices:
        raise ValueError

    print(sorted_list)

g = AdjacencySetGraph(9, directed=True)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(3, 4)
g.add_edge(6, 8)

topological_sort(g)