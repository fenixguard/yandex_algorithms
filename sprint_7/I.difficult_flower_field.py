from typing import List


def solution(n: int, m: int, flowers: List[List[str]]):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]) + flowers[i][j]

    print(dp[0][n])

    path = []
    i = 0
    j = n

    while i != m - 1 or j != 1:
        if dp[i][j - 1] >= dp[i + 1][j] and j != 1:
            path.append('R')
            j -= 1
        else:
            path.append('U')
            i += 1

    return "".join(reversed(path))


def input_data():
    m, n = map(int, input().strip().split())
    flowers = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        flowers[i] = [0] + list(map(int, list(input())))

    return n, m, flowers


if __name__ == '__main__':
    print(solution(*input_data()))
