from typing import Tuple


def power(x, n, I, mult):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = power(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


def fib(n, k):
    F = power([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][0] % 10 ** k


def input_data() -> Tuple[int, int]:
    n, k = map(int, input().strip().split())
    return n, k


if __name__ == '__main__':
    print(fib(*input_data()))
