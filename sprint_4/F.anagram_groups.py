from typing import NoReturn
from collections import defaultdict, Counter


def solution(words: list) -> NoReturn:
    anagrams = defaultdict(list)
    for i, word in enumerate(words):
        histogram = frozenset(Counter(word).items())
        anagrams[histogram].append(i)

    for i in anagrams.values():
        print(*i)


def input_data() -> list:
    n = int(input())
    words = input().strip().split()
    return words


if __name__ == '__main__':
    solution(input_data())

"""
6
tan eat tea ate nat bat

"""