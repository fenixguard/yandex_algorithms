from typing import Tuple


def is_sub_sequence(first_str: str, second_str: str, length_first_str: int, length_second_str: int):
    j = 0
    i = 0
    while j < length_first_str and i < length_second_str:
        if first_str[j] == second_str[i]:
            j += 1
        i += 1

    return j == length_first_str


def solution(first_str: str, second_str: str):
    length_first_str = len(first_str)
    length_second_str = len(second_str)
    print("True" if is_sub_sequence(first_str, second_str, length_first_str, length_second_str) else "False")


def input_data() -> Tuple[str, str]:
    s = input()
    t = input()
    return s, t


if __name__ == '__main__':
    solution(*input_data())
