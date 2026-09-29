class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def update(n):
    n.height = 1 + max(height(n.left), height(n.right))

def rotate_right(y):
    x = y.left
    middle = x.right
    x.right = y
    y.left = middle
    update(y)
    update(x)
    return x

def rotate_left(x):
    y = x.right
    middle = y.left
    y.left = x
    x.right = middle
    update(x)
    update(y)
    return y

def insert(n, key):
    if n is None:
        return Node(key)
    if key < n.key:
        n.left = insert(n.left, key)
    elif key > n.key:
        n.right = insert(n.right, key)
    else:
        return n

    update(n)
    balance = height(n.left) - height(n.right)

    if balance > 1:
        if key > n.left.key:
            n.left = rotate_left(n.left)
        return rotate_right(n)

    if balance < -1:
        if key < n.right.key:
            n.right = rotate_right(n.right)
        return rotate_left(n)

    return n

root = None
for key in [30, 20, 10]:
    root = insert(root, key)

print(root.key, root.left.key, root.right.key)