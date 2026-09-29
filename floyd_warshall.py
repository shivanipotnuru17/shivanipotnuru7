def floyd_warshall(vertices, edges):
    inf = float("inf")
    dist = {
        u: {
            v: (0 if u == v else inf)
            for v in vertices
        }
        for u in vertices
    }

    for u, v, weight in edges:
        dist[u][v] = min(dist[u][v], weight)

    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    if any(dist[v][v] < 0 for v in vertices):
        raise ValueError("Negative cycle")

    return dist

names = ["A", "B", "C"]

result = floyd_warshall(
    names,
    [("A", "B", 3), ("B", "C", 2), ("A", "C", 10)]
)

for name in names:
    print(name, [result[name][v] for v in names])