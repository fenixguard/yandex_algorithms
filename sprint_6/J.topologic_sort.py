from typing import List, Tuple


class Graph:
    def __init__(self, n):
        self.size = n
        self.edges = [[] for _ in range(n + 1)]
        self.color = ['white'] * (self.size + 1)
        self.order = []

    def add_edge(self, v, w):
        self.edges[v].append(w)

    def top_sort(self, vertex):

        self.color[vertex] = 'gray'
        for w in self.edges[vertex]:
            if self.color[w] == 'white':
                self.top_sort(w)
        self.color[vertex] = 'black'
        self.order.append(vertex)


def solution(n: int, edges: List[Tuple[int, int]]):
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    for i in range(1, n + 1):
        if graph.color[i] == 'white':
            graph.top_sort(i)

    print(*reversed(graph.order))


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
5 3
3 2
3 4
2 5

6 3
6 4
4 1
5 1

"""
