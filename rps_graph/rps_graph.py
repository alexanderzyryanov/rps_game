from collections import defaultdict


class RPSGraph:

    def __init__(self):
        self._graph = defaultdict(set)

    def extend(self, vertex, vertices_to, vertices_from):
        if vertex in self._graph:
            return ValueError()

        vertices_to = set(vertices_to)
        vertices_from = set(vertices_from)
        if vertices_to & vertices_from:
            raise ValueError()

        graph_vertices = set(self._graph)
        new_edge_vertices = vertices_to | vertices_from
        if new_edge_vertices ^ graph_vertices:
            raise ValueError()

        self._graph[vertex].update(vertices_to)

        for vertex_from in vertices_from:
            self._graph[vertex_from].add(vertex)
