from flow_edge import FlowEdge


class FlowNetwork:
    """
    Rede de fluxo direcionada representada por listas de adjacência.

    Segue a estrutura de Graph da base algs4-py:
    - mesmo atributo V (número de vértices)
    - mesmo atributo E (número de arestas)
    - mesmo atributo adj (lista de listas de adjacência)
    - mesma assinatura __str__

    Diferença em relação a Graph: add_edge adiciona a mesma FlowEdge
    nas duas listas de adjacência (origem e destino), permitindo
    percorrer arestas residuais nos dois sentidos.
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
        """
        Adiciona a aresta e nas listas de adjacência dos dois extremos.
        A mesma instância aparece em adj[v] e adj[w], permitindo
        que residual_capacity_to e add_residual_flow_to operem nos dois sentidos.
        """
        v = e.From()
        w = e.To()
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.E += 1
