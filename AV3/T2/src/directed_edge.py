class DirectedEdge:
    """
    Representa uma aresta direcionada com peso em um grafo valorado.
    Baseado na interface DirectedEdge do livro Algorithms, 4th Edition (algs4).

    Cada aresta possui uma cidade de origem (v), uma cidade de destino (w)
    e um preço/peso (weight) associado ao voo.
    """

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def from_vertex(self):
        """Retorna a cidade de origem do voo."""
        return self.v

    def to_vertex(self):
        """Retorna a cidade de destino do voo."""
        return self.w

    def get_weight(self):
        """Retorna o preço do voo."""
        return self.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __repr__(self):
        return f"{self.v}->{self.w} (peso={self.weight})"
