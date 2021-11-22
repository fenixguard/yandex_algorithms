# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def print_paths(root):
    total_sum = []
    path = []
    print_paths_rec(root, path, 0, total_sum)
    return total_sum


def print_paths_rec(root, path, path_lenght, total_sum):
    total_sum = total_sum
    if root is None:
        return

    if len(path) > path_lenght:
        path[path_lenght] = str(root.value)
    else:
        path.append(str(root.value))

    path_lenght += 1

    if root.left is None and root.right is None:
        total_sum.append(tuple(path))
    else:
        print_paths_rec(root.left, path, path_lenght, total_sum)
        print_paths_rec(root.right, path, path_lenght, total_sum)


def print_array(arr, lenght):
    temp = ""
    for i in arr[0:lenght]:
        temp += i
    print(temp)


def solution(root):
    t_s = 0
    for pr in print_paths(root):
        temp = ""
        for i in range(len(pr)):
            temp += pr[i]
        t_s += int(temp)
    return t_s

