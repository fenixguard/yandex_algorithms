from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int, n: int, m: int) -> List[int]:
    up_elem = None
    down_elem = None
    left_elem = None
    right_elem = None
    if n == m == 1:
        return []

    if row == 0:
        if n > 1:
            down_elem = matrix[row + 1][col]
        if col == 0:
            if m > 1:
                right_elem = matrix[row][col + 1]

        elif col == m - 1:
            if m > 1:
                left_elem = matrix[row][col - 1]
        else:
            left_elem = matrix[row][col - 1]
            right_elem = matrix[row][col + 1]
    elif row == n - 1:
        if n > 1:
            up_elem = matrix[row - 1][col]
        if col == 0:
            if m > 1:
                right_elem = matrix[row][col + 1]
        elif col == m - 1:
            if m > 1:
                left_elem = matrix[row][col - 1]
        else:
            left_elem = matrix[row][col - 1]
            right_elem = matrix[row][col + 1]
    else:
        if n > 1:
            up_elem = matrix[row - 1][col]
            down_elem = matrix[row + 1][col]
        if col == 0:
            if m > 1:
                right_elem = matrix[row][col + 1]
        elif col == m - 1:
            if m > 1:
                left_elem = matrix[row][col - 1]
        else:
            left_elem = matrix[row][col - 1]
            right_elem = matrix[row][col + 1]

    elements = list(filter(lambda x: x is not None, [up_elem, down_elem, left_elem, right_elem]))

    return elements


def read_input() -> Tuple[List[List[int]], int, int, int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col, n, m


matrix, row, col, n, m = read_input()
print(" ".join(map(str, sorted(get_neighbours(matrix, row, col, n, m)))))
