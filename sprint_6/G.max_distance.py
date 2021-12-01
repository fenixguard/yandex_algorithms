from typing import List, Tuple
from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.size = n
        self.edges = defaultdict(list)
        self.color = ['white'] * (self.size + 1)
        self.distance = [None] * (self.size + 1)
        self.previous = [None] * (self.size + 1)

    def add_edge(self, v, w):
        self.edges[v].append(w)
        self.edges[w].append(v)

    def bfs(self, vertex):
        planned = deque()
        planned.append(vertex)
        self.color[vertex] = 'grey'
        self.distance[vertex] = 0
        while len(planned) != 0:
            u = planned.popleft()
            for v in sorted(self.edges[u]):
                if self.color[v] == 'white':
                    self.distance[v] = self.distance[u] + 1
                    self.previous[v] = u
                    self.color[v] = 'gray'
                    planned.append(v)
            self.color[u] = 'black'


def solution(n: int, edges: List[Tuple[int, int]], start_vertex: int):
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    graph.bfs(start_vertex)
    print(max(graph.distance[1:]))


def input_data():
    n, m = map(int, input().strip().split())
    rows = m
    edges = list()
    while rows:
        edges.append(tuple(map(int, input().strip().split())))
        rows -= 1
    start_vertex = int(input())
    return n, edges, start_vertex


if __name__ == '__main__':
    solution(*input_data())

"""
5 4
2 1
4 5
4 3
3 2
2

3 3
3 1
1 2
2 3
1

"""
