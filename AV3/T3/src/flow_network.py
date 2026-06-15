"""
FlowNetwork - Grafo de fluxo com lista de adjacencia de FlowEdge
Inspirado em FlowNetwork.java do algs4 (Sedgewick & Wayne, 4a edicao)
"""

from flow_edge import FlowEdge


class FlowNetwork:
    def __init__(self, V):
        self._V   = V
        self._adj = [[] for _ in range(V)]

    def V(self):
        return self._V

    def add_edge(self, e: FlowEdge):
        v = e.from_vertex()
        w = e.to_vertex()
        self._adj[v].append(e)   # aresta direta em v
        self._adj[w].append(e)   # mesma aresta em w (acesso reverso)

    def adj(self, v):
        return self._adj[v]
