"""
Directed weighted graph implementation.
Vertices are represented as integers from 0 to V-1.
Edges are directed and carry integer weights.
"""


class DiGraph:
    """
    A directed weighted graph using adjacency list representation.
    """

    def __init__(self, v):
        """
        Initialize a digraph with v vertices.
        
        Args:
            v: Number of vertices (0 to v-1)
        """
        self.V = v
        self.E = 0
        # adj[v] is a list of tuples (w, weight) representing edges v->w
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v, w, weight):
        """
        Add a directed edge from v to w with given weight.
        Allows parallel edges (multiple edges between same pair).
        
        Args:
            v: Source vertex
            w: Destination vertex
            weight: Edge weight (integer)
        """
        if not (0 <= v < self.V and 0 <= w < self.V):
            raise ValueError(f"Vertex out of range: {v} or {w}")
        
        self.adj[v].append((w, weight))
        self.E += 1

    def __str__(self):
        """String representation of the graph."""
        lines = [f"{self.V} vertices, {self.E} edges"]
        for v in range(self.V):
            edges_str = " ".join(f"({w},{weight})" for w, weight in self.adj[v])
            lines.append(f"{v}: {edges_str}")
        return "\n".join(lines)

    def get_in_degree(self, v):
        """Return in-degree of vertex v."""
        count = 0
        for u in range(self.V):
            for w, _ in self.adj[u]:
                if w == v:
                    count += 1
        return count

    def get_out_degree(self, v):
        """Return out-degree of vertex v (length of adjacency list)."""
        return len(self.adj[v])

    def get_balance(self, v):
        """
        Return balance of vertex v: out_degree - in_degree.
        For an Eulerian circuit to exist, all vertices must have balance = 0.
        """
        return self.get_out_degree(v) - self.get_in_degree(v)
