"""
    Start at smallest edge and keep taking them as long as they are not connected to node. Repeat untill all nodes are visited
    Time complexity O(ElogE)
"""


# Kruskal's Algorithm for Minimum Spanning Tree (Simplified)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, node):
        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v  # Union

def kruskal(n, edges):
    # Sort edges by weight (O(E log E))
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):  # If u and v are in different components
            uf.union(u, v)  # Union the sets
            mst.append((u, v, weight))  # Add edge to MST
            total_weight += weight

    return mst, total_weight

# Example usage
if __name__ == "__main__":
    # Number of vertices
    n = 5

    # List of edges (u, v, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst, mst_weight = kruskal(n, edges)

    print(f"Edges in MST: {mst}")
    print(f"Total weight of MST: {mst_weight}")
