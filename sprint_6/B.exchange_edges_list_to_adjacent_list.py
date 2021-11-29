from typing import List, Tuple


def create_adjacent_list(edges):
    adjacent_list = dict()
    for edge in edges:
        if adjacent_list.get(edge[0]):
            adjacent_list[edge[0]].append(edge[1])
        else:
            adjacent_list[edge[0]] = [edge[1]]
    return adjacent_list


def solution(n: int, m: int, edges: List[Tuple[int, int]]):
    adjacents_list = create_adjacent_list(edges)
    for i in range(1, n + 1):
        temp = [0] * n
        if adjacents_list.get(i):
            vertex = adjacents_list.get(i)
            for v in vertex:
                temp[v - 1] = 1
        print(' '.join(map(str, temp)))



def input_data():
    n, m = map(int, input().strip().split())
    rows = m
    edges = list()
    while rows:
        edges.append(tuple(map(int, input().strip().split())))
        rows -= 1
    return n, m, edges


if __name__ == '__main__':
    solution(*input_data())

"""
5 3
1 3
2 3
5 2

"""
