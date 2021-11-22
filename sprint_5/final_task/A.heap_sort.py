from typing import List, NoReturn, Tuple


def heapify(members: List[Tuple[int, int, str]], n: int, i: int) -> NoReturn:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and members[i] < members[left]:
        largest = left
    if right < n and members[largest] < members[right]:
        largest = right

    if largest != i:
        members[i], members[largest] = members[largest], members[i]
        heapify(members, n, largest)


def heap_sort(members: List[Tuple[int, int, str]], n: int) -> NoReturn:

    for i in range(n, -1, -1):
        heapify(members, n, i)

    for i in range(n - 1, 0, -1):
        members[i], members[0] = members[0], members[i]
        heapify(members, i, 0)


def print_members_name(members: List[Tuple[int, int, str]]) -> NoReturn:
    n = len(members)
    heap_sort(members, n)
    for i in range(n):
        print(members[i][2])


def input_data() -> List[Tuple[int, int, str]]:
    n = int(input())
    members = []
    while n:
        name, p, f = input().strip().split()
        members.append((-int(p), int(f), name))
        n -= 1
    return members


if __name__ == '__main__':
    print_members_name(input_data())

"""
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80

5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0
"""
