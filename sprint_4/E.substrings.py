from typing import NoReturn


def solution(row: str) -> NoReturn:
    checklist = {}
    starting_index_of_current_substring = 0
    length_of_longest_substring = 0
    for i, v in enumerate(row):
        if v in checklist:
            if checklist[v] >= starting_index_of_current_substring:
                starting_index_of_current_substring = checklist[v] + 1
        length_of_current_substring = i - starting_index_of_current_substring + 1
        length_of_longest_substring = max(length_of_current_substring, length_of_longest_substring)
        checklist[v] = i

    print(length_of_longest_substring)


def input_data() -> str:
    row = input().strip()
    return row


if __name__ == '__main__':
    solution(input_data())
