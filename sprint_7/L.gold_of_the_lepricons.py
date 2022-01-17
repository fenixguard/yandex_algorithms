from typing import List
import copy


def solution(n: int, m: int, golds: List[int]):
    dp = [[0] * (m + 1) for _ in range(2)]
    idx = 0
    idx_prev = 1
    for i in range(n):
        gold = golds[i]
        dp[idx] = copy.copy(dp[idx_prev])
        for j in range(gold, m + 1):
            dp[idx][j] = dp[idx_prev][j] \
                if dp[idx_prev][j] > (gold + dp[idx_prev][j - gold]) \
                else (gold + dp[idx_prev][j - gold])

        idx, idx_prev = idx_prev, idx

    return dp[idx_prev][m]


def input_data():
    n, m = map(int, input().strip().split())
    golds = sorted(map(int, input().strip().split()))

    return n, m, golds


if __name__ == '__main__':
    print(solution(*input_data()))
