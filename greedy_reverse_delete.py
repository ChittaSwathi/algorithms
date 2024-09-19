"""
    Delete the laregest edge from given graph and keep doing as long as all nodes are still connected.
    Time complexity - O(E⋅(V+E))
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store all edges

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor, _ in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_connected(self):
        # Check if the graph is connected by performing DFS
        visited = [False] * self.V
        self.dfs(0, visited)
        return all(visited)  # If all vertices are visited, the graph is connected

    def build_adjacency_list(self):
        # Build an adjacency list from the current edges
        self.adj_list = {i: [] for i in range(self.V)}
        for u, v, w in self.graph:
            self.adj_list[u].append((v, w))
            self.adj_list[v].append((u, w))

    def reverse_delete_mst(self):
        # Sort all edges in decreasing order by weight
        self.graph.sort(key=lambda x: x[2], reverse=True)

        mst = []  # To store the MST edges
        self.build_adjacency_list()  # Build adjacency list from the graph

        # Iterate over the sorted edges
        for u, v, w in self.graph[:]:
            # Remove edge from the adjacency list
            self.adj_list[u].remove((v, w))
            self.adj_list[v].remove((u, w))

            if not self.is_connected():  # If removing the edge disconnects the graph
                # Add edge back to MST and adjacency list
                mst.append((u, v, w))
                self.adj_list[u].append((v, w))
                self.adj_list[v].append((u, w))

        return mst

# Example usage
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)

    # Add edges: (u, v, weight)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst = g.reverse_delete_mst()

    print(f"Edges in MST: {mst}")
