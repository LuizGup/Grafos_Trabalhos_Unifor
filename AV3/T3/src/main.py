"""
UVa 11045 - My T-shirt suits me
Modelagem como rede de fluxo, resolvida com Ford-Fulkerson (DFS).
"""

import sys
from flow_edge import FlowEdge
from flow_network import FlowNetwork
from ford_fulkerson import FordFulkerson

SIZES = {'XXL': 0, 'XL': 1, 'L': 2, 'M': 3, 'S': 4, 'XS': 5}


def solve():
    data = sys.stdin.read().split('\n')
    idx  = 0
    T    = int(data[idx]); idx += 1

    for _ in range(T):
        N, M = map(int, data[idx].split()); idx += 1
        shirts_per_size = N // 6

        # Nos:
        #   0        = fonte
        #   1..6     = tamanhos (XXL=1, XL=2, L=3, M=4, S=5, XS=6)
        #   7..7+M-1 = voluntarios
        #   7+M      = sorvedouro
        SOURCE = 0
        SINK   = 7 + M

        G = FlowNetwork(SINK + 1)

        # fonte -> cada tamanho
        for size_id in range(6):
            G.add_edge(FlowEdge(SOURCE, size_id + 1, shirts_per_size))

        # tamanho -> voluntario + voluntario -> sorvedouro
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
