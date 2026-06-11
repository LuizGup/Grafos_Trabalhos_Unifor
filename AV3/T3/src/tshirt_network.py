from flow_network import FlowNetwork
from flow_edge import FlowEdge

SIZES = {'XXL': 0, 'XL': 1, 'L': 2, 'M': 3, 'S': 4, 'XS': 5}
NUM_SIZES = 6


def build_network(N: int, M: int, preferences: list) -> tuple:
    """
    Constrói a rede de fluxo para o problema de distribuição de camisetas.

    Layout dos nós:
        0         -> fonte (source)
        1..6      -> tamanhos (XXL=1, XL=2, L=3, M=4, S=5, XS=6)
        7..7+M-1  -> voluntários
        7+M       -> sorvedouro (sink)

    Arestas (FlowEdge):
        source  -> tamanho[i]     capacidade = N/6
        tamanho -> voluntário[j]  capacidade = 1  (se o tamanho serve ao voluntário)
        voluntário -> sink         capacidade = 1
    """
    num_nodes = 1 + NUM_SIZES + M + 1
    source = 0
    sink = 7 + M

    G = FlowNetwork(num_nodes)
    shirts_per_size = N // NUM_SIZES

    # source -> cada tamanho
    for i in range(NUM_SIZES):
        G.add_edge(FlowEdge(source, 1 + i, shirts_per_size))

    # tamanho -> voluntário + voluntário -> sink
    for j, (s1, s2) in enumerate(preferences):
        volunteer = 7 + j
        G.add_edge(FlowEdge(1 + SIZES[s1], volunteer, 1))
        G.add_edge(FlowEdge(1 + SIZES[s2], volunteer, 1))
        G.add_edge(FlowEdge(volunteer, sink, 1))

    return G, source, sink
