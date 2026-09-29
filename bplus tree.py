class Leaf:
    def __init__(self, keys):
        self.keys = keys
        self.next = None

class Internal:
    def __init__(self, children):
        self.children = children
        self.keys = [first(c) for c in children[1:]]

def first(node):
    while isinstance(node, Internal):
        node = node.children[0]
    return node.keys[0]

def build(keys, leaf_size=2, fanout=3):
    keys = sorted(set(keys))

    if not keys:
        return None

    leaves = [
        Leaf(keys[i:i + leaf_size])
        for i in range(0, len(keys), leaf_size)
    ]

    for left, right in zip(leaves, leaves[1:]):
        left.next = right

    level = leaves

    while len(level) > 1:
        level = [
            Internal(level[i:i + fanout])
            for i in range(0, len(level), fanout)
        ]

    return level[0]

def leaf_for(root, key):
    node = root

    while isinstance(node, Internal):
        i = 0

        while i < len(node.keys) and key >= node.keys[i]:
            i += 1

        node = node.children[i]

    return node

def range_keys(root, low, high):
    if root is None:
        return []

    node = leaf_for(root, low)
    result = []

    while node is not None:
        for key in node.keys:
            if key > high:
                return result
            if key >= low:
                result.append(key)

        node = node.next

    return result

root = build([2, 5, 8, 11, 14, 17])

print(root.keys)
print(11 in leaf_for(root, 11).keys)
print(range_keys(root, 5, 14))