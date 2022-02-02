from typing import List


def solution(first: str, second: str):
    first_length = len(first)
    second_length = len(second)
    if abs(first_length - second_length) >= 2:
        return False

    max_length = max(first_length, second_length)

    i = 0
    j = 0

    diff = 0
    while i < max_length and j < max_length:
        try:
            if first[i] == second[j]:
                i += 1
                j += 1
                continue
            elif first[i] != second[j] and second_length != first_length:
                if first_length > second_length:
                    i += 1
                else:
                    j += 1

                diff += 1
            else:
                diff += 1
                i += 1
                j += 1
        except IndexError:
            if first_length > second_length:
                i += 1
            else:
                j += 1

            diff += 1

        if diff > 1:
            return False

    return True


def input_data():
    first = input().strip()
    second = input().strip()
    return first, second


if __name__ == '__main__':
    answer = solution(*input_data())
    if answer:
        print('OK')
    else:
        print('FAIL')
