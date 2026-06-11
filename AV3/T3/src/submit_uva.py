import sys
from collections import deque

# --- FlowEdge Class ---
class FlowEdge:
    """
    Aresta de fluxo direcionada com capacidade e fluxo atual.
    """
    def __init__(self, v, w, capacity):
        self.v = v
        self.w = w
        self.capacity = capacity
        self.flow = 0

    def __str__(self):
        return "%d->%d %d/%d" % (self.v, self.w, self.flow, self.capacity)

    def From(self):
        return self.v

    def To(self):
        return self.w

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise Exception("invalid edge")

    def residual_capacity_to(self, vertex):
        if vertex == self.w:
            return self.capacity - self.flow
        elif vertex == self.v:
            return self.flow
        else:
            raise Exception("invalid edge")

    def add_residual_flow_to(self, vertex, delta):
        if vertex == self.w:
            self.flow += delta
        elif vertex == self.v:
            self.flow -= delta
        else:
            raise Exception("invalid edge")


# --- FlowNetwork Class ---
class FlowNetwork:
    """
    Rede de fluxo direcionada representada por listas de adjacência.
    """
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(self.V)]

    def __str__(self):
        lines = ["%d vertices, %d edges" % (self.V, self.E)]
        for v in range(self.V):
            neighbors = " ".join(str(e) for e in self.adj[v])
            lines.append("%d: %s" % (v, neighbors))
        return "\n".join(lines)

    def add_edge(self, e: FlowEdge):
        v = e.From()
        w = e.To()
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.E += 1


# --- BreadthFirstPaths Class ---
class BreadthFirstPaths:
    """
    BFS no grafo residual para encontrar caminho aumentante.
    """
    def __init__(self, G: FlowNetwork, s: int):
        self._marked = [False] * G.V
        self.edge_to = [None] * G.V
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


# --- FordFulkerson Class ---
class FordFulkerson:
    """
    Algoritmo de Ford-Fulkerson com BFS (Edmonds-Karp).
    """
    def __init__(self, G: FlowNetwork, s: int, t: int):
        self.value = 0
        self._in_cut = [False] * G.V

        bfs = BreadthFirstPaths(G, s)
        while bfs.has_path_to(t):
            path = bfs.path_to(t)

            bottle = float('inf')
            x = t
            for e in reversed(path):
                bottle = min(bottle, e.residual_capacity_to(x))
                x = e.other(x)

            x = t
            for e in reversed(path):
                e.add_residual_flow_to(x, bottle)
                x = e.other(x)

            self.value += bottle
            bfs = BreadthFirstPaths(G, s)

        for v in range(G.V):
            self._in_cut[v] = bfs.has_path_to(v)

    def in_cut(self, v: int) -> bool:
        return self._in_cut[v]


# --- T-shirt Network Construction ---
SIZES = {'XXL': 0, 'XL': 1, 'L': 2, 'M': 3, 'S': 4, 'XS': 5}
NUM_SIZES = 6

def build_network(N: int, M: int, preferences: list) -> tuple:
    num_nodes = 1 + NUM_SIZES + M + 1
    source = 0
    sink = 7 + M

    G = FlowNetwork(num_nodes)
    shirts_per_size = N // NUM_SIZES

    for i in range(NUM_SIZES):
        G.add_edge(FlowEdge(source, 1 + i, shirts_per_size))

    for j, (s1, s2) in enumerate(preferences):
        volunteer = 7 + j
        G.add_edge(FlowEdge(1 + SIZES[s1], volunteer, 1))
        G.add_edge(FlowEdge(1 + SIZES[s2], volunteer, 1))
        G.add_edge(FlowEdge(volunteer, sink, 1))

    return G, source, sink


# --- Main ---
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    T = int(data[idx]); idx += 1

    for _ in range(T):
        if idx >= len(data):
            break
        N = int(data[idx]); idx += 1
        M = int(data[idx]); idx += 1

        preferences = []
        for _ in range(M):
            s1 = data[idx]; idx += 1
            s2 = data[idx]; idx += 1
            preferences.append((s1, s2))

        G, source, sink = build_network(N, M, preferences)
        ff = FordFulkerson(G, source, sink)

        print("YES" if ff.value == M else "NO")

if __name__ == "__main__":
    main()
