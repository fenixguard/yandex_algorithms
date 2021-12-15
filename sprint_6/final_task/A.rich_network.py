from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple
import heapq


@dataclass
class Edge:
    v: int
    u: int
    w: int

    def __init__(self, *args):
        self.v = args[1]
        self.u = args[2]
        self.w = args[0]


class Graph:

    def __init__(self, size):
        self.size = size + 1
        self.graph = defaultdict(list)
        self.vertices = set()
        self.maximum_spanning_tree = 0
        self.added = set()       # Множество вершин, уже добавленных в остов.
        self.not_added = set()   # Множество вершины, ещё не добавленных в остов.
        self.edges = []          # Массив рёбер, исходящих из остовного дерева.

    def add_edge(self, u, v, w):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def filter(self, vertex):
        temp = []
        for s_v in self.graph.get(vertex):
            if s_v[0] in self.not_added:
                temp.append((s_v[1], vertex, s_v[0]))
        return temp

    def add_vertex(self, vertex):
        self.added.add(vertex)
        self.not_added.remove(vertex)
        items = self.filter(vertex)
        if items:
            for item in items:
                heapq.heappush(self.edges, item)

    def extract_minimum(self):
        return heapq.heappop(self.edges)

    def find_mst(self, m):
        if m == 0 and self.size - 1 == 1:
            return 0
        self.not_added = self.vertices
        vertex = list(self.vertices)[0]
        self.add_vertex(vertex)
        while self.not_added and self.edges:
            edge = Edge(*self.extract_minimum())
            if edge.u in self.not_added:
                self.maximum_spanning_tree += edge.w
                self.add_vertex(edge.u)

        if self.not_added:
            return "Oops! I did it again"
        else:
            return abs(self.maximum_spanning_tree)


def solution(n: int, edges: List[Tuple[int, int]], m: int):
    if m == 0 and n > 1:
        print("Oops! I did it again")
        return
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1], -edge[2])
    print(graph.find_mst(m))


def input_data():
    n, m = map(int, input().strip().split())
    rows = m
    edges = list()
    while rows:
        edges.append(tuple(map(int, input().strip().split())))
        rows -= 1
    return n, edges, m


if __name__ == '__main__':
    solution(*input_data())

"""
4 2
1 2 3
3 4 4

4 4
1 2 5
1 3 6
2 4 8
3 4 3

3 3
1 2 1
1 2 2
2 3 1

2 0

"""
