from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    length_first = len(first_number)
    length_second = len(second_number)
    second_number_list = []
    first_number_list = []
    if length_first > length_second:
        first_number_list = [int(s) for s in first_number]

        second_number_list.extend([0] * (length_first - length_second))
        second_number_list.extend([int(s) for s in second_number])

    elif length_first < length_second:
        second_number_list = [int(s) for s in second_number]

        first_number_list.extend([0] * (length_second - length_first))
        first_number_list.extend([int(s) for s in first_number])

    else:
        first_number_list = [int(s) for s in first_number]
        second_number_list = [int(s) for s in second_number]

    result_number_list = [0] * (len(first_number_list) + 1)
    for i in range(len(first_number_list) - 1, -1, -1):
        result = first_number_list[i] + second_number_list[i] + result_number_list[i + 1]
        if result == 0 or result == 1:
            result_number_list[i + 1] = result
        elif result == 2:
            result_number_list[i + 1] = 0
            result_number_list[i] = 1
        else:
            result_number_list[i + 1] = 1
            result_number_list[i] = 1
    if result_number_list[0] == 0:
        del result_number_list[0]
    return ''.join(map(str, result_number_list))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
