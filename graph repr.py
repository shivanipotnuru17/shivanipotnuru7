vertices = ["A", "B", "C"]
edges = [("A", "B"), ("A", "C"), ("B", "C")]

graph = {v: [] for v in vertices}

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

index = {v: i for i, v in enumerate(vertices)}
matrix = [[0] * len(vertices) for _ in vertices]

for u, v in edges:
    matrix[index[u]][index[v]] = 1
    matrix[index[v]][index[u]] = 1

print(graph)

for row in matrix:
    print(row)