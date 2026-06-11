from collections import deque
from flow_network import FlowNetwork


class BreadthFirstPaths:
    """
    BFS no grafo residual para encontrar caminho aumentante de s até t.

    Segue rigorosamente a estrutura de BreadthFirstPaths da base algs4-py:
    - mesmo atributo _marked (visitados)
    - mesmo atributo edge_to (aresta que chegou em cada vértice)
    - mesmos métodos: bfs(), has_path_to(), path_to()

    Diferença: edge_to armazena FlowEdge (não inteiros), pois precisamos
    das arestas para calcular o gargalo e atualizar o fluxo residual.
    O critério de visita usa residual_capacity_to > 0 em vez de
    simplesmente "não visitado", pois só seguimos arestas com capacidade residual.
    """

    def __init__(self, G: FlowNetwork, s: int):
        self._marked = [False] * G.V
        self.edge_to = [None] * G.V  # edge_to[v] = FlowEdge que chegou em v
        self.s = s
        self._bfs(G, s)

    def _bfs(self, G: FlowNetwork, s: int):
        self._marked[s] = True
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for e in G.adj[v]:
                w = e.other(v)
                if not self._marked[w] and e.residual_capacity_to(w) > 0:
                    self.edge_to[w] = e
                    self._marked[w] = True
                    queue.append(w)

    def has_path_to(self, v: int) -> bool:
        return self._marked[v]

    def path_to(self, v: int):
        """Retorna lista de FlowEdges do caminho de s até v, ou None se não existe."""
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self.s:
            e = self.edge_to[x]
            path.append(e)
            x = e.other(x)
        path.reverse()
        return path
