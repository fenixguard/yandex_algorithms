

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(root, key: int):
    if root is None:
        return root
    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)

        root.value = temp.value
        root.right = remove(root.right, temp.value)
    return root
