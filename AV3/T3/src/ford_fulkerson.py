from flow_network import FlowNetwork
from breadth_first_paths import BreadthFirstPaths


class FordFulkerson:
    """
    Algoritmo de Ford-Fulkerson com BFS (Edmonds-Karp) para fluxo máximo.

    Usa BreadthFirstPaths (da base algs4-py) para encontrar caminhos
    aumentantes no grafo residual. A cada iteração:
      1. BFS encontra caminho de s a t com capacidade residual > 0
      2. Calcula o gargalo (mínima capacidade residual no caminho)
      3. Atualiza o fluxo em cada aresta do caminho via add_residual_flow_to

    Complexidade: O(V * E^2) — Edmonds-Karp garante no máximo O(V*E) iterações,
    cada BFS custa O(V+E).
    """

    def __init__(self, G: FlowNetwork, s: int, t: int):
        self.value = 0
        self._in_cut = [False] * G.V

        # Enquanto houver caminho aumentante, envia fluxo
        bfs = BreadthFirstPaths(G, s)
        while bfs.has_path_to(t):
            path = bfs.path_to(t)

            # Calcula o gargalo do caminho
            bottle = float('inf')
            x = t
            for e in reversed(path):
                bottle = min(bottle, e.residual_capacity_to(x))
                x = e.other(x)

            # Atualiza fluxo em cada aresta
            x = t
            for e in reversed(path):
                e.add_residual_flow_to(x, bottle)
                x = e.other(x)

            self.value += bottle
            bfs = BreadthFirstPaths(G, s)

        # Marca vértices no lado da fonte no corte mínimo
        for v in range(G.V):
            self._in_cut[v] = bfs.has_path_to(v)

    def in_cut(self, v: int) -> bool:
        """Retorna True se o vértice v está no lado da fonte no corte mínimo."""
        return self._in_cut[v]
