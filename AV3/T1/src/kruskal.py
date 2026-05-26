import sys
from edge import Edge
from uf import UF


# ──────────────────────────────────────────────────────────────
# INTEGRANTE 1 — Parser de entrada
# ──────────────────────────────────────────────────────────────

def ler_casos():
    """
    Lê todos os casos de teste do stdin e retorna uma lista de tuplas
    (n, edges), onde n é o número de vértices e edges é a lista de
    objetos Edge com os pesos inteiros do problema.

    Formato de entrada esperado (UVA 10600):
        T
        N M
        A1 B1 C1
        ...
        AM BM CM
    """
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx]); idx += 1
    casos = []

    for _ in range(t):
        n = int(data[idx]); m = int(data[idx + 1]); idx += 2
        edges = []
        for _ in range(m):
            a = int(data[idx])
            b = int(data[idx + 1])
            c = int(data[idx + 2])
            idx += 3
            edges.append(Edge(a, b, c))
        casos.append((n, edges))

    return casos


# ──────────────────────────────────────────────────────────────
# INTEGRANTE 2 — Algoritmo de Kruskal
# ──────────────────────────────────────────────────────────────

def kruskal(n, edges, edge_to_skip=None):
    """
    Executa o algoritmo de Kruskal sobre uma lista de arestas pré-ordenada.

    Parâmetros
    ----------
    n            : número de vértices (vértices numerados de 1 a n)
    edges        : lista de objetos Edge ordenada em ordem crescente de peso
    edge_to_skip : objeto Edge a ser ignorado nesta execução (usado para
                   encontrar a Segunda MST); None para a MST original

    Retorno
    -------
    (custo, arestas_da_mst)  se for possível formar uma árvore geradora
    (float('inf'), [])       se o grafo ficar desconectado ao ignorar a aresta
    """
    # Vértices são 1-indexados, então alocamos n+1 posições no UF
    uf = UF(n + 1)
    mst_edges = []
    mst_weight = 0

    # Complexidade: O(M·α(N)) — cada aresta passa uma vez pelo UF quase-constante
    for edge in edges:
        if edge is edge_to_skip:
            continue

        v = edge.either()
        w = edge.other(v)

        if not uf.connected(v, w):
            uf.union(v, w)
            mst_edges.append(edge)
            mst_weight += edge.weight

    # Caso especial: grafo desconectado — menos de n-1 arestas significa que
    # dois vértices ficaram em componentes separadas (aresta de corte removida)
    if len(mst_edges) < n - 1:
        return float('inf'), []

    return mst_weight, mst_edges
