import sys
from heapq import heappush, heappop

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); m = int(data[pos+1]); k = int(data[pos+2])
    pos += 3

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(data[pos]); b = int(data[pos+1]); c = int(data[pos+2])
        pos += 3
        adj[a].append((b, c))
        radj[b].append((a, c))

    # Passo 1: Dijkstra reverso — rev[v] = menor distância de v até n
    INF = float('inf')
    rev = [INF] * (n + 1)
    rev[n] = 0
    h = [(0, n)]
    while h:
        d, u = heappop(h)
        if d > rev[u]:
            continue
        for v, w in radj[u]:
            nd = d + w
            if nd < rev[v]:
                rev[v] = nd
                heappush(h, (nd, v))

    # Passo 2: Transformar pesos com função potencial
    # w'(u,v) = w(u,v) + rev[v] - rev[u] >= 0
    # Isso embute o A* nos pesos, permitindo tuplas de 2 elementos no heap
    pot1 = rev[1]
    for u in range(n + 1):
        if rev[u] >= INF:
            adj[u] = []
            continue
        new_adj = []
        ru = rev[u]
        for v, w in adj[u]:
            rv = rev[v]
            if rv < INF:
                new_adj.append((v, w + rv - ru))
        adj[u] = new_adj

    # Passo 3: K menores caminhos com pesos reduzidos + poda kth
    kth = [INF] * (n + 1)
    cnt = [0] * (n + 1)
    h = [(0, 1)]
    res = []

    while h:
        d, u = heappop(h)
        if d >= kth[u]:
            continue
        cnt[u] += 1
        if cnt[u] == k:
            kth[u] = d
        if u == n:
            res.append(d + pot1)  # converter de volta para custo real
            if len(res) == k:
                break
        for v, w in adj[u]:
            nd = d + w
            if nd < kth[v]:
                heappush(h, (nd, v))

    sys.stdout.write(' '.join(map(str, res)) + '\n')

main()
