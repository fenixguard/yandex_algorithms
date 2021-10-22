from typing import List, Tuple


def lbin_search(l, r, check_params):
    seq, x = check_params
    while l < r:
        m = (l + r) // 2
        if seq[m] >= x:
            r = m
        else:
            l = m + 1
    return l


def find(search, n, seq, x):
    ans = search(0, n - 1, (seq, x))
    if seq[ans] >= x:
        return ans + 1
    return -1


def solution(n: int, days: List[int], price: int) -> Tuple[int, int]:
    price_one_cycle = price
    price_two_cycle = price * 2
    result_1 = find(lbin_search, n, days, price_one_cycle)
    result_2 = find(lbin_search, n, days, price_two_cycle)
    return result_1, result_2


def input_data() -> Tuple[int, List[int], int]:
    n = int(input())
    days = list(map(int, input().strip().split()))
    s = int(input())
    return n, days, s


if __name__ == '__main__':
    print(*solution(*input_data()))
