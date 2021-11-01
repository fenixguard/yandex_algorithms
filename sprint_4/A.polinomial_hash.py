from typing import Tuple, NoReturn


def solution(a: int, m: int, row: str) -> NoReturn:
    hash_sum = 0
    for r in row:
        hash_sum = (hash_sum * a + ord(r)) % m

    print(hash_sum)


def input_data() -> Tuple[int, int, str]:
    a = int(input())
    m = int(input())
    row = input().strip()
    return a, m, row


if __name__ == '__main__':
    solution(*input_data())
