from typing import List
import copy


def solution(n: int, m: int, sequence_1: List[int], sequence_2: List[int]):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if sequence_1[i - 1] == sequence_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    if n == 0 or m == 0:
        print(0)
    else:
        answer = []
        first = []
        second = []
        i = n
        j = m

        while dp[i][j] != 0:
            if sequence_1[i - 1] == sequence_2[j - 1]:
                answer.append(sequence_1[i - 1])
                first.append(i)
                second.append(j)
                i -= 1
                j -= 1
                continue
            elif dp[i][j] == dp[i - 1][j]:
                i -= 1
                continue
            elif dp[i][j] == dp[i][j - 1]:
                j -= 1
                continue

        print(dp[n][m])

        if dp[n][m] > 0:
            print(" ".join(map(str, reversed(first))))
            print(" ".join(map(str, reversed(second))))


def input_data():
    n = int(input())
    sequence_1 = list(map(int, input().strip().split()))
    m = int(input())
    sequence_2 = list(map(int, input().strip().split()))

    return n, m, sequence_1, sequence_2


if __name__ == '__main__':
    solution(*input_data())
