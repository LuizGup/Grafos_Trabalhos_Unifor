import sys
from math import inf


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
        if vertex == self._v:
            return self._flow
        elif vertex == self._w:
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


class FlowNetwork:
    def __init__(self, V):
        self._V   = V
        self._adj = [[] for _ in range(V)]

    def V(self):
        return self._V

    def add_edge(self, e):
        v = e.from_vertex()
        w = e.to_vertex()
        self._adj[v].append(e)
        self._adj[w].append(e)

    def adj(self, v):
        return self._adj[v]


class FordFulkerson:
    def __init__(self, G, s, t):
        self._value   = 0
        self._marked  = None
        self._edge_to = None

        while self._has_augmenting_path(G, s, t):
            bottle = inf
            v = t
            while v != s:
                bottle = min(bottle, self._edge_to[v].residual_capacity_to(v))
                v = self._edge_to[v].other(v)

            v = t
            while v != s:
                self._edge_to[v].add_residual_flow_to(v, bottle)
                v = self._edge_to[v].other(v)

            self._value += bottle

    def _has_augmenting_path(self, G, s, t):
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


SIZES = {'XXL': 0, 'XL': 1, 'L': 2, 'M': 3, 'S': 4, 'XS': 5}

def solve():
    data = sys.stdin.read().split('\n')
    idx  = 0
    T    = int(data[idx]); idx += 1

    for _ in range(T):
        N, M = map(int, data[idx].split()); idx += 1
        shirts_per_size = N // 6

        SOURCE = 0
        SINK   = 7 + M

        G = FlowNetwork(SINK + 1)

        for size_id in range(6):
            G.add_edge(FlowEdge(SOURCE, size_id + 1, shirts_per_size))

        for i in range(M):
            parts = data[idx].split(); idx += 1
            s1, s2 = parts[0], parts[1]
            vol = 7 + i
            G.add_edge(FlowEdge(SIZES[s1] + 1, vol, 1))
            G.add_edge(FlowEdge(SIZES[s2] + 1, vol, 1))
            G.add_edge(FlowEdge(vol, SINK, 1))

        ff = FordFulkerson(G, SOURCE, SINK)
        print("YES" if ff.value() == M else "NO")

solve()
