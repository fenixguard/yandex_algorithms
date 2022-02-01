from typing import List


def solution(data: List[str]):
    print(" ".join(reversed(data)))


def input_data():
    data = input().strip().split()
    return data


if __name__ == '__main__':
    solution(input_data())
