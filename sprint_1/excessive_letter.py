from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    short_dict = dict()
    long_dict = dict()
    for s in shorter:
        if short_dict.get(s):
            short_dict[s] += 1
        else:
            short_dict[s] = 1
    for s in longer:
        if long_dict.get(s):
            long_dict[s] += 1
        else:
            long_dict[s] = 1

    for ch in longer:
        short_char = short_dict.get(ch)
        long_char = long_dict.get(ch)
        if short_char:
            if short_char != long_char:
                return ch
        else:
            return ch


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
