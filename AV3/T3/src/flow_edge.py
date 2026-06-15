"""
FlowEdge - Aresta com capacidade e fluxo
Inspirado em FlowEdge.java do algs4 (Sedgewick & Wayne, 4a edicao)
"""


class FlowEdge:
    def __init__(self, v, w, capacity):
        self._v        = v
        self._w        = w
        self._capacity = capacity
        self._flow     = 0

    def from_vertex(self):
        return self._v

    def to_vertex(self):
        return self._w

    def capacity(self):
        return self._capacity

    def flow(self):
        return self._flow

    def other(self, vertex):
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise ValueError("Vertex invalido")

    def residual_capacity_to(self, vertex):
        if vertex == self._v:        # aresta reversa
            return self._flow
        elif vertex == self._w:      # aresta direta
            return self._capacity - self._flow
        else:
            raise ValueError("Vertex invalido")

    def add_residual_flow_to(self, vertex, delta):
        if vertex == self._v:
            self._flow -= delta
        elif vertex == self._w:
            self._flow += delta
        else:
            raise ValueError("Vertex invalido")
