import heapq

def dijkstra(graph, start):
    distance = {v: float("inf") for v in graph}
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)

        if cost != distance[u]:
            continue

        for v, weight in graph[u]:
            if weight < 0:
                raise ValueError("Negative edge")

            candidate = cost + weight

            if candidate < distance[v]:
                distance[v] = candidate
                heapq.heappush(heap, (candidate, v))

    return distance

g = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 5)],
    "D": []
}

print(dijkstra(g, "A"))