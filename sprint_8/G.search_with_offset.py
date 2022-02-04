from typing import List


def find(search: List[int], pattern: List[int], start: int) -> int:
    result = -1

    if start >= len(search):
        return result

    if len(search) - start < len(pattern):
        return result

    for pos in range(start, len(search) - len(pattern) + 1):
        shift = None
        match = True

        for offset in range(len(pattern)):
            if shift is None:
                shift = pattern[offset] - search[pos]

            if search[pos + offset] + shift != pattern[offset]:
                match = False
                break

        if match:
            result = pos + 1
            break

    return result


def solution(search: List[int], pattern: List[int]):
    occurrences = []

    len_pattern = len(pattern)
    len_search = len(search)

    if len_pattern > len_search:
        return occurrences

    start = 0

    while True:
        pos = find(search, pattern, start)

        if pos == -1:
            break

        occurrences.append(pos)
        start = pos

    return occurrences


def input_data():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    m = int(input().strip())
    match = list(map(int, input().strip().split()))
    return arr, match


if __name__ == '__main__':
    answer = solution(*input_data())
    print(' '.join(map(str, answer)))
