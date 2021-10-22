from typing import Tuple, List


def solution(n: int, arr: List[int]):
    sorted_arr = True
    for i in range(n):
        exchange_flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchange_flag = True
                sorted_arr = False

        if sorted_arr:
            return 1
        elif exchange_flag:
            print(*arr)
        else:
            return 0


def input_data() -> Tuple[int, List[int]]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return n, arr


if __name__ == '__main__':
    n, arr = input_data()
    if solution(n, arr):
        print(*arr)
