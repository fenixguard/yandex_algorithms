alphabet = {
    "b",
    "d",
    "f",
    "h",
    "j",
    "l",
    "n",
    "p",
    "r",
    "t",
    "v",
    "x",
    "z",
}


def solution(first: str, second: str):
    new_first_string = ''
    new_second_string = ''
    for f in first:
        if f in alphabet:
            new_first_string += f
    for s in second:
        if s in alphabet:
            new_second_string += s

    if new_first_string < new_second_string:
        print(-1)
    elif new_first_string == new_second_string:
        print(0)
    else:
        print(1)


def input_data():
    first = input().strip()
    second = input().strip()
    return first, second


if __name__ == '__main__':
    solution(*input_data())
