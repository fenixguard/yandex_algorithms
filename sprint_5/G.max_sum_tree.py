# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def find_max(root) -> int:
    if root is None:
        return 0
    left = find_max(root.left)
    right = find_max(root.right)

    max_single = max(max(left, right) + root.value, root.value)
    max_top = max(max_single, left + right + root.value)
    find_max.res = max(find_max.res, max_top)
    return max_single


def solution(root) -> int:
    find_max.res = float("-inf")
    find_max(root)
    return find_max.res
