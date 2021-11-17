from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def insert(root, key):
    if root is None:
        return Node(value=key)
    else:
        if root.value == key and root.left is None and root.right is None:
            root.right = Node(value=key)
            return root
        elif key >= root.value:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
