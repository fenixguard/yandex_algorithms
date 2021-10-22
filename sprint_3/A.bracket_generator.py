from typing import NoReturn


def gen_brackets(n: int, count_open: int, count_close: int, ans: str) -> NoReturn:
    if count_open + count_close == 2 * n:
        print(ans)
        return
    if count_open < n:
        gen_brackets(n, count_open + 1, count_close, ans + '(')
    if count_open > count_close:
        gen_brackets(n, count_open, count_close + 1, ans + ')')


def solution(n: int) -> NoReturn:
    gen_brackets(n, 0, 0, '')


def input_data() -> int:
    n = int(input())
    return n


if __name__ == '__main__':
    solution(input_data())
