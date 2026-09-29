import heapq

def prim(graph, start):
    visited = {start}
    heap = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(heap)
    chosen = []

    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)
        chosen.append((u, v, weight))

        for neighbor, cost in graph[v]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost, v, neighbor))

    if len(visited) != len(graph):
        raise ValueError("Graph is disconnected")

    return chosen, sum(w for _, _, w in chosen)

graph = {
    "A": [("B", 1), ("C", 3)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 3), ("B", 2), ("D", 4)],
    "D": [("B", 5), ("C", 4)]
}

print(prim(graph, "A"))