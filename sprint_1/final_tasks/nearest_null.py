"""
ID успешного решения: 54192402
"""
from typing import List, Tuple


def nearest_null(n: int, sequence: List[int]) -> List[int]:
    free_places_index = []
    for i, s in enumerate(sequence):
        if s == 0:
            free_places_index.append(i)
    left_free_place_index = free_places_index[0]
    right_free_place_index = free_places_index[-1]
    result_dist = [0] * n
    if len(free_places_index) == 1:
        for i in range(left_free_place_index, len(sequence)):  # Проход вправо
            if sequence[i] == 0:
                result_dist[i] = 0
            else:
                result_dist[i] = result_dist[i - 1] + 1
        for i in reversed(range(left_free_place_index + 1)):  # Проход влево
            if sequence[i] == 0:
                result_dist[i] = 0
            else:
                result_dist[i] = result_dist[i + 1] + 1
        return result_dist

    if len(free_places_index) == n:
        return result_dist

    for i in range(left_free_place_index, len(sequence)):  # Проход вправо до индекса правого пустого места
        if sequence[i] == 0:
            result_dist[i] = 0
        else:
            result_dist[i] = result_dist[i - 1] + 1
    for i in range(right_free_place_index, left_free_place_index, -1):  # Проход влево до индекса левого пустого места
        if sequence[i] == 0:
            result_dist[i] = 0
        else:
            result_dist[i] = min(result_dist[i], result_dist[i + 1] + 1)
    for i in reversed(range(left_free_place_index + 1)):  # Проход влево от левого пустого места до начала массива
        if sequence[i] == 0:
            result_dist[i] = 0
        else:
            result_dist[i] = result_dist[i + 1] + 1

    return result_dist


def read_input() -> Tuple[int, List[int]]:
    with open('input.txt') as input_file:
        n = int(input_file.readline().strip())
        sequence = list(map(int, input_file.readline().strip().split()))

    return n, sequence


result = nearest_null(*read_input())
with open('output.txt', 'w') as out_file:
    out_file.write(" ".join(map(str, result)))

