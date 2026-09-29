def kruskal(vertices, edges):
    parent = {v: v for v in vertices}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    chosen = []

    for weight, u, v in sorted(edges):
        a, b = find(u), find(v)

        if a != b:
            parent[a] = b
            chosen.append((u, v, weight))

    if len(chosen) != len(vertices) - 1:
        raise ValueError("Graph is disconnected")

    return chosen, sum(w for _, _, w in chosen)

vertices = ["A", "B", "C", "D"]

edges = [
    (1, "A", "B"),
    (2, "B", "C"),
    (3, "A", "C"),
    (4, "C", "D"),
    (5, "B", "D")
]

print(kruskal(vertices, edges))