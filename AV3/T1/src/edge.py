class Edge:
    """
    Representa uma aresta não-direcionada com peso em um grafo valorado.
    Baseado na interface Edge do livro Algorithms, 4th Edition (algs4).
    """

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        """Retorna um dos extremos da aresta."""
        return self.v

    def other(self, vertex):
        """Retorna o extremo oposto ao vértice informado."""
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise ValueError(f"Vértice {vertex} não pertence a esta aresta ({self.v}-{self.w})")

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __repr__(self):
        return f"{self.v}-{self.w} (peso={self.weight})"
