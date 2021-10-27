from typing import List, Tuple, NoReturn


def solution(first_str: str, second_str: str) -> NoReturn:
    if len(first_str) != len(second_str):
        return "NO"
    mapping = dict()
    if len(first_str) >= len(second_str):
        max_str = first_str
        min_str = second_str
    else:
        max_str = second_str
        min_str = first_str
    uniq_chars = set()
    for i, c in enumerate(max_str):
        if i > len(min_str) - 1:
            if not mapping.get(c):
                return "NO"
        else:
            char = mapping.get(c)
            if not char:
                if min_str[i] in uniq_chars:
                    return "NO"
                else:
                    mapping[c] = min_str[i]
                    uniq_chars.add(min_str[i])
            else:
                if char != min_str[i]:
                    return "NO"
    return "YES"


def input_data() -> Tuple[str, str]:
    first_str = input().strip()
    second_str = input().strip()
    return first_str, second_str


if __name__ == '__main__':
    print(solution(*input_data()))
