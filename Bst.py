class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def contains(root, value):
    while root is not None:
        if value == root.value:
            return True
        root = root.left if value < root.value else root.right
    return False

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

root = None
for key in [8, 3, 10, 1, 6]:
    root = insert(root, key)

print(inorder(root))
print(contains(root, 6), contains(root, 9))