"""
Hierholzer's algorithm for finding Eulerian circuits in directed graphs.
"""


class DirectedEulerianCycle:
    """
    Finds an Eulerian circuit in a directed graph using Hierholzer's algorithm.
    An Eulerian circuit is a closed walk that visits every edge exactly once.
    
    For an Eulerian circuit to exist:
    - The graph must be strongly connected (or have edges only within connected components)
    - Every vertex must have in-degree == out-degree
    """

    def __init__(self, digraph):
        """
        Initialize with a directed graph.
        
        Args:
            digraph: A DiGraph object
        """
        self.digraph = digraph
        self.circuit = []
        self.total_weight = 0
        self._has_eulerian_circuit = self._check_and_find_circuit()

    def _check_and_find_circuit(self):
        """
        Check if Eulerian circuit exists and find it.
        
        Returns:
            True if circuit was found, False otherwise
        """
        # Check if all vertices have balance == 0
        for v in range(self.digraph.V):
            if self.digraph.get_balance(v) != 0:
                return False

        # Find a starting vertex that has outgoing edges
        start = None
        for v in range(self.digraph.V):
            if self.digraph.get_out_degree(v) > 0:
                start = v
                break

        if start is None:
            return False

        # Create a copy of adjacency list for traversal
        adj_copy = [list(neighbors) for neighbors in self.digraph.adj]

        # Hierholzer's algorithm using stack
        stack = [start]
        circuit_path = []

        while stack:
            v = stack[-1]
            if adj_copy[v]:
                # Take next edge from v
                w, weight = adj_copy[v].pop()
                stack.append(w)
                self.total_weight += weight
            else:
                # No more edges from v, add to circuit
                circuit_path.append(stack.pop())

        # Circuit is built in reverse order
        self.circuit = circuit_path[::-1]

        # Verify that all edges were used
        # (circuit should traverse all E edges, visiting V+1 vertices if all edges used once)
        # For Eulerian circuit: len(circuit) - 1 should equal number of edges
        if len(self.circuit) - 1 != self.digraph.E:
            return False

        return True

    def has_eulerian_circuit(self):
        """Return True if an Eulerian circuit exists."""
        return self._has_eulerian_circuit

    def get_circuit(self):
        """
        Return the Eulerian circuit as a list of vertices.
        Circuit starts and ends at the same vertex.
        """
        return self.circuit if self._has_eulerian_circuit else None

    def get_total_weight(self):
        """Return the total weight of the Eulerian circuit."""
        return self.total_weight if self._has_eulerian_circuit else None
