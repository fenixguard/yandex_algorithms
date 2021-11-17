# Comment it before submitting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_max(node):
    if not node:
        return float("-inf")
    max_left = tree_max(node.left)
    max_right = tree_max(node.right)
    return max(node.value, max_left, max_right)


def tree_min(node):
    if not node:
        return float("inf")
    min_left = tree_min(node.left)
    min_right = tree_min(node.right)
    return min(node.value, min_left, min_right)


def solution(root) -> bool:
    if not root:
        return True
    if (tree_max(root.left) < root.value < tree_min(root.right) and solution(root.left) and solution(root.right)):
        return True
    return False


def test():
    node1 = TreeNode(1, None, None)
    node2 = TreeNode(4, None, None)
    node3 = TreeNode(3, node1, node2)
    node4 = TreeNode(8, None, None)
    node5 = TreeNode(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)
