# Comment it before submitting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(root) -> int:
    values = list()

    def recurse(node):
        if node:
            values.append(node.value)
            if node.left:
                recurse(node.left)
            if node.right:
                recurse(node.right)

    recurse(root)
    return max(values)


def test():
    node1 = TreeNode(1)
    node2 = TreeNode(-5)
    node3 = TreeNode(3, node1, node2)
    node4 = TreeNode(2, node3, None)
    assert solution(node4) == 3
