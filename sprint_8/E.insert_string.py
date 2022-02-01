
from typing import List, Tuple


def solution(s: str, words: List[Tuple[str, int]]):
    new = ''
    offset = 0
    for word, pos in sorted(words, key=lambda x: x[1]):
        new += s[offset:pos] + word
        offset = pos

    new += s[offset:]
    print(new)


def input_data():
    s = input().strip()
    n = int(input().strip())
    words = []
    while n:
        word, num = input().strip().split()
        words.append((word, int(num)))
        n -= 1
    return s, words


if __name__ == '__main__':
    solution(*input_data())
