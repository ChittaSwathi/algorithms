"""
    Equivalent to Kruskals algorithm finding an MST and deleting the k-1 most expensive edges.
    Time complexity - O(n**2 logn)
"""

import heapq
import math

# Helper class for Union-Find (Disjoint Set Union)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Single-link k-clustering function
def single_link_k_clustering(points, k):
    n = len(points)
    uf = UnionFind(n)

    # Priority queue (min-heap) to store the distances between all pairs of points
    min_heap = []

    # Initialize the heap with all pairwise distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            heapq.heappush(min_heap, (dist, i, j))

    clusters_count = n

    # Keep merging clusters until we have exactly k clusters
    while clusters_count > k:
        # Get the closest pair of points
        dist, u, v = heapq.heappop(min_heap)

        # Check if they belong to different clusters
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            clusters_count -= 1

    # Group points by their cluster
    clusters = {}
    for i in range(n):
        root = uf.find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(points[i])

    return list(clusters.values())

# Example usage
if __name__ == "__main__":
    # Sample points (2D coordinates)
    points = [
        (0, 0), (1, 1), (1, 0), (4, 4), (5, 5), (6, 6)
    ]
    k = 2

    clusters = single_link_k_clustering(points, k)

    print(f"{k} clusters: {clusters}")
