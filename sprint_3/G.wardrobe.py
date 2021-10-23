from typing import List


def solution(things: List[str]):
    pink = []
    yellow = []
    raspberry = []
    for i in things:
        if i == "0":
            pink.append("0")
        elif i == "1":
            yellow.append("1")
        else:
            raspberry.append("2")

    print(" ".join(pink + yellow + raspberry))


def input_data() -> List[str]:
    n = int(input())
    things = list(input().strip().split())
    return things


if __name__ == '__main__':
    solution(input_data())
