"""
    Choose any node and select its smallest edge. Now keep selecting for smallest edge connected to these nodes. Keep until all nodes are visited.
    time complexity - O(Elogn)
"""



import heapq

def prim(graph, start=0):
    n = len(graph)  # Number of vertices
    mst = []  # List to store edges in the MST
    visited = [False] * n  # Track visited vertices
    min_heap = [(0, start, -1)]  # (cost, vertex, previous_vertex)

    total_weight = 0

    while min_heap:
        cost, current_vertex, previous_vertex = heapq.heappop(min_heap)

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True
        total_weight += cost

        if previous_vertex != -1:  # Skip the initial node
            mst.append((previous_vertex, current_vertex, cost))

        # Add all edges from current_vertex to the heap
        for neighbor, weight in graph[current_vertex]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor, current_vertex))

    return mst, total_weight

# Example usage
if __name__ == "__main__":
    # Graph represented as adjacency list
    graph = {
        0: [(1, 10), (2, 6), (3, 5)],
        1: [(0, 10), (3, 15)],
        2: [(0, 6), (3, 4)],
        3: [(0, 5), (1, 15), (2, 4)]
    }

    mst, total_weight = prim(graph)

    print(f"Edges in MST: {mst}")
    print(f"Total weight of MST: {total_weight}")
