from typing import List, Tuple
from sys import setrecursionlimit

setrecursionlimit(10000)


class Graph:
    def __init__(self, n):
        self.size = n
        self.edges = [[] for _ in range(n + 1)]
        self.color = [-1] * (self.size + 1)
        self.component_color = 1

    def add_edge(self, v, w):
        self.edges[v].append(w)
        self.edges[w].append(v)

    def comp_sort(self, vertex):
        for w in self.edges[vertex]:
            if self.color[w] == -1:
                self.color[w] = self.component_color
                self.comp_sort(w)
        self.color[vertex] = self.component_color


def solution(n: int, edges: List[Tuple[int, int]]):
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    for i in range(1, n + 1):
        if graph.color[i] == -1:
            graph.comp_sort(i)
            graph.component_color += 1
    count_dict = dict()
    for i, color in enumerate(graph.color[1:], start=1):
        if count_dict.get(color):
            count_dict[color].append(i)
        else:
            count_dict[color] = [i]
    print(len(count_dict.keys()))
    for _, v in sorted(count_dict.items(), key=lambda x: x[1]):
        print(*(sorted(v)))


def input_data():
    n, m = map(int, input().strip().split())
    rows = m
    edges = list()
    while rows:
        edges.append(tuple(map(int, input().strip().split())))
        rows -= 1
    return n, edges


if __name__ == '__main__':
    solution(*input_data())

"""
6 4
1 2
6 5
2 3
3 4

2 0

"""
