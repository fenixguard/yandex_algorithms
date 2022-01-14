from typing import List, Tuple

MOD = 10 ** 9 + 7


def solution(n: int, k: int):
    steps = [0, 1] + [0] * (n - 1)

    for stair in range(2, n + 1):
        for step in range(1, k + 1):
            if step <= stair:
                steps[stair] += steps[stair - step]
        steps[stair] = steps[stair] % MOD

    return steps[n]



def input_data():
    n, k = map(int, input().strip().split())

    return n, k


if __name__ == '__main__':
    print(solution(*input_data()))

"""
6 3

7 7

2 2

"""
