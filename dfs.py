def dfs(graph, start):
    seen = set()
    order = []

    def visit(node):
        if node in seen:
            return

        seen.add(node)
        order.append(node)

        for neighbor in graph[node]:
            visit(neighbor)

    visit(start)
    return order

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

print(dfs(graph, "A"))