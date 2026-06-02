import sys
from directed_edge import DirectedEdge


# ──────────────────────────────────────────────────────────────
# INTEGRANTE 1 — Representação do Grafo e Parser de Entrada
# ──────────────────────────────────────────────────────────────

def ler_entrada():
    """
    Lê a entrada do stdin e retorna o grafo como lista de adjacência,
    junto com os parâmetros do problema.

    Formato de entrada esperado (CSES 1196 - Flight Routes):
        n m k
        a1 b1 c1
        a2 b2 c2
        ...
        am bm cm

    Retorno
    -------
    (adj, n, k)
        adj : lista de adjacência — adj[v] contém os DirectedEdge saindo de v
        n   : número de cidades (destino é a cidade n)
        k   : quantidade de menores rotas a encontrar
    """
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); m = int(data[idx + 1]); k = int(data[idx + 2])
    idx += 3

    # Lista de adjacência: cidades numeradas de 1 a n
    # Índice 0 fica vazio para manter a indexação natural
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        idx += 3
        adj[a].append(DirectedEdge(a, b, c))

    return adj, n, k
