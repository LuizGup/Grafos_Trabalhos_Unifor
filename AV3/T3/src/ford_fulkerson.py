"""
FordFulkerson - Fluxo maximo com DFS (caminhos aumentantes)
Inspirado em FordFulkerson.java do algs4 (Sedgewick & Wayne, 4a edicao)
"""

from math import inf
from flow_network import FlowNetwork


class FordFulkerson:
    def __init__(self, G: FlowNetwork, s: int, t: int):
        self._value   = 0
        self._marked  = None
        self._edge_to = None

        while self._has_augmenting_path(G, s, t):
            # capacidade de gargalo (bottleneck) do caminho encontrado
            bottle = inf
            v = t
            while v != s:
                bottle = min(bottle, self._edge_to[v].residual_capacity_to(v))
                v = self._edge_to[v].other(v)

            # aumenta fluxo ao longo do caminho
            v = t
            while v != s:
                self._edge_to[v].add_residual_flow_to(v, bottle)
                v = self._edge_to[v].other(v)

            self._value += bottle

    def _has_augmenting_path(self, G: FlowNetwork, s: int, t: int):
        """DFS iterativa no grafo residual — busca caminho de s ate t."""
        self._marked  = [False] * G.V()
        self._edge_to = [None]  * G.V()

        stack = [s]
        self._marked[s] = True

        while stack:
            v = stack.pop()
            if v == t:
                return True
            for e in G.adj(v):
                w = e.other(v)
                if not self._marked[w] and e.residual_capacity_to(w) > 0:
                    self._marked[w]  = True
                    self._edge_to[w] = e
                    stack.append(w)

        return self._marked[t]

    def value(self):
        return self._value
