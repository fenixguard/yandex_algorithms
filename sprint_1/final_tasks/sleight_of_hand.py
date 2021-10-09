"""
ID успешного решения: 54192576
"""
from typing import Dict, Set, Tuple


def sleight_of_hand(k: int, field_buttons: Dict[int, int], rounds: Set[int]) -> int:
    max_points = 0
    press_buttons = k * 2
    for r in rounds:
        count_button = field_buttons.get(r)
        if count_button <= press_buttons:
            max_points += 1
    return max_points


def read_input() -> Tuple[int, Dict[int, int], Set[int]]:
    k = int(input())
    field_buttons = dict()
    rounds = set()
    for i in range(4):
        row = input().strip()
        for r in row:
            if r.isdigit():
                num = int(r)
                if field_buttons.get(num):
                    field_buttons[num] += 1
                else:
                    field_buttons[num] = 1
                rounds.add(num)

    return k, field_buttons, rounds


result = sleight_of_hand(*read_input())
print(result)
