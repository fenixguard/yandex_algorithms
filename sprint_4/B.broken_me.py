from typing import Tuple, NoReturn
import random
import string
import secrets
from tqdm import tqdm


def gen_string():
    num = 16
    return ''.join(secrets.choice(string.ascii_lowercase) for _ in range(num))


def solution(a: int, m: int) -> NoReturn:
    hash_sum_1 = 0
    hash_list_1 = []
    row_1 = gen_string()
    n1 = len(row_1)
    for i, r in enumerate(row_1):
        hash_sum_1 += ord(r) * a ** (n1 - i - 1)
        hash_list_1.append(ord(r) * a ** (n1 - i - 1))
    hash_sum_1 = hash_sum_1 % m

    for _ in tqdm(range(100_000_000)):
        row_2 = gen_string()
        hash_list_2 = []
        hash_sum_2 = 0
        n2 = len(row_2)
        for i, r in enumerate(row_2):
            hash_sum_2 += ord(r) * a ** (n2 - i - 1)
            hash_list_2.append(ord(r) * a ** (n2 - i - 1))
        hash_sum_2 = hash_sum_2 % m
        if hash_sum_1 == hash_sum_2:
            print("RESULT")
            print(row_1)
            print(row_2)
            print("RESULT")


def input_data() -> Tuple[int, int]:
    # a = int(input())
    # m = int(input())
    return 1000, 123987123


if __name__ == '__main__':
    solution(*input_data())
"""
asphivtbukvnmhci -> 21813000
ldtvoazivebggwyg -> 21813000
"""