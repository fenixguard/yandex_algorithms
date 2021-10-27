from typing import List


def solution(arr: List[str]):
    society = dict()
    for a in arr:
        soc = society.get(a)
        if not soc:
            society[a] = 1
            print(a)


def input_data() -> List[str]:
    n = int(input())
    arr = []
    while n:
        arr.append(input())
        n -= 1
    return arr


if __name__ == '__main__':
    solution(input_data())
