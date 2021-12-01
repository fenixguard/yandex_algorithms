from typing import List, Tuple


class Graph:
    def __init__(self, n):
        self.size = n
        self.edges = [[] for _ in range(n + 1)]
        self.color = ['white'] * (self.size + 1)

    def add_edge(self, v, w):
        self.edges[v].append(w)
        self.edges[w].append(v)

    def dfs(self, start_vertex):

        stack = list()
        stack.append(start_vertex)
        while len(stack) != 0:
            v = stack.pop()
            if self.color[v] == 'white':
                print(v, end=' ')
                self.color[v] = 'gray'
                stack.append(v)
                for w in sorted(self.edges[v], reverse=True):
                    if self.color[w] == 'white':
                        stack.append(w)
            elif self.color[v] == 'gray':
                self.color[v] = 'black'


def solution(n: int, edges: List[Tuple[int, int]], start_vertex: int):
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    graph.dfs(start_vertex)


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
4 4
3 2
4 3
1 4
1 2
3

2 1
1 2
1

"""
