"""
    Unlike dijikstras, bellman ford can even work with negative weighted edges
    Time complexity - O(V*E)
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Early exit if no changes are made in a full iteration
        for _ in range(self.V - 1):
            changed = False
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:
                break  # Exit early if no update was made

        # Check for negative weight cycle
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return None

        return dist
