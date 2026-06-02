import heapq


# ──────────────────────────────────────────────────────────────
# INTEGRANTE 2 — Dijkstra Modificado para K Menores Caminhos
# ──────────────────────────────────────────────────────────────

def k_shortest_paths(adj, n, k):
    """
    Encontra os k menores custos de rota da cidade 1 até a cidade n,
    usando uma variação do algoritmo de Dijkstra.

    Conceito (baseado no DijkstraSP do algs4):
    - No Dijkstra clássico, cada vértice é processado uma única vez e
      mantém-se um vetor distTo[] atualizado via relaxamento.
    - Aqui, permitimos que cada vértice seja extraído da fila de prioridade
      até k vezes. A j-ésima extração do destino n corresponde ao j-ésimo
      menor custo de rota.

    Fila de prioridade:
    - Usamos heapq (fila de prioridade mínima nativa do Python), permitida
      pelo enunciado do trabalho.
    - Cada entrada na fila é uma tupla (dist, v), onde dist é o custo
      acumulado até o vértice v.

    Parâmetros
    ----------
    adj : lista de adjacência — adj[v] contém os DirectedEdge saindo de v
    n   : número de cidades (destino é a cidade n)
    k   : quantidade de menores rotas a encontrar

    Retorno
    -------
    Lista com os k menores custos de rota de 1 até n.
    """
    # count[v] = quantas vezes o vértice v já foi extraído da fila
    count = [0] * (n + 1)

    # Fila de prioridade mínima: (custo acumulado, vértice)
    # Inicializa com a cidade de origem 1 e custo 0
    heap = [(0, 1)]

    # Lista para armazenar os k menores custos até o destino n
    resultado = []

    # Complexidade: O(k · m · log(k · m))
    # Cada vértice pode ser extraído até k vezes; cada extração
    # relaxa suas arestas adjacentes e insere na fila.
    while heap and len(resultado) < k:
        dist, u = heapq.heappop(heap)

        count[u] += 1

        # Se este vértice já foi extraído k vezes, não precisamos
        # processá-lo novamente — já temos k caminhos passando por ele
        if count[u] > k:
            continue

        # Se chegamos ao destino, registramos o custo
        if u == n:
            resultado.append(dist)

        # Relaxamento: para cada aresta saindo de u
        for edge in adj[u]:
            v = edge.to_vertex()
            w = edge.get_weight()

            # Só insere na fila se v ainda não foi extraído k vezes
            # (poda essencial para evitar crescimento descontrolado da fila)
            if count[v] < k:
                heapq.heappush(heap, (dist + w, v))

    return resultado
