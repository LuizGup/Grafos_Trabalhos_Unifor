class UF:
    """
    Estrutura Union-Find (Disjoint Set Union) com:
    - União por rank: mantém a árvore balanceada anexando a menor sob a maior.
    - Compressão de caminhos por divisão (path halving): durante o find, cada
      nó aponta para o avô, reduzindo progressivamente a altura da árvore.

    Baseado no WeightedQuickUnionUF do livro Algorithms, 4th Edition (algs4).
    """

    def __init__(self, n):
        """Inicializa n elementos, cada um em seu próprio conjunto."""
        self.count = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, p):
        """Retorna o representante (raiz) do conjunto que contém p."""
        while self.parent[p] != p:
            # Compressão de caminho por divisão: aponta para o avô
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        """Une os conjuntos de p e q."""
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        # Une pela rank: arvore de menor rank fica abaixo da maior
        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        else:
            self.parent[root_q] = root_p
            self.rank[root_p] += 1
        self.count -= 1

    def connected(self, p, q):
        """Retorna True se p e q pertencem ao mesmo conjunto."""
        return self.find(p) == self.find(q)
