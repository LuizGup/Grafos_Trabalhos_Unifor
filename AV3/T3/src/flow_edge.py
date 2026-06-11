class FlowEdge:
    """
    Aresta de fluxo direcionada com capacidade e fluxo atual.

    Inspirada em Edge e DirectedEdge da base algs4-py:
    - usa v (origem) e w (destino) como atributos, igual a Edge/DirectedEdge
    - métodos From() e To() seguem a convenção de DirectedEdge
    - método other(v) segue a convenção de Edge

    Cada aresta armazena o fluxo atual (flow) e a capacidade (capacity).
    A capacidade residual é capacity - flow na direção direta,
    e flow na direção reversa (permite cancelamento de fluxo).
    """

    def __init__(self, v, w, capacity):
        self.v = v
        self.w = w
        self.capacity = capacity
        self.flow = 0

    def __str__(self):
        return "%d->%d %d/%d" % (self.v, self.w, self.flow, self.capacity)

    def From(self):
        """Retorna o vértice de origem da aresta (convenção de DirectedEdge)."""
        return self.v

    def To(self):
        """Retorna o vértice de destino da aresta (convenção de DirectedEdge)."""
        return self.w

    def other(self, vertex):
        """Retorna o outro extremo da aresta dado um vértice (convenção de Edge)."""
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise Exception("invalid edge")

    def residual_capacity_to(self, vertex):
        """
        Capacidade residual na direção do vértice dado:
        - Se vertex é o destino (w): capacidade ainda disponível (capacity - flow)
        - Se vertex é a origem (v): fluxo já enviado, que pode ser cancelado
        """
        if vertex == self.w:
            return self.capacity - self.flow
        elif vertex == self.v:
            return self.flow
        else:
            raise Exception("invalid edge")

    def add_residual_flow_to(self, vertex, delta):
        """
        Envia delta unidades de fluxo na direção do vértice:
        - direção direta (v->w): aumenta o fluxo
        - direção reversa (w->v): diminui o fluxo (cancelamento)
        """
        if vertex == self.w:
            self.flow += delta
        elif vertex == self.v:
            self.flow -= delta
        else:
            raise Exception("invalid edge")
