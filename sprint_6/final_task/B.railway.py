"""
ID успешной посылки: 63250362
-------------------------------------------------------------------------------
Задача:
Определить является ли сеть железных дорог оптимальной. Под оптимальностью
понимается, что от одного города до другого можно проехать только по маршруту,
состоящему исключительно из дорог типа R или только из дорог типа B.
-------------------------------------------------------------------------------
Алгоритм:
Первая версия алгоритма была похожа на полный перебор всех путей с их хранением.
Естественно эта версия не прошла по памяти, а где-то и по времени. Но она была
отправной точкой, чтобы подумать как все это улучшить. Второй алгоритм был
освнован на временах входа-выхода при DFS. Но тут я запутался и пока пытался
разобраться уже забыл идею реализации с проверкой путей. Третий вариант -
тот что получилось реализовать, а как оказалось он самый простой из всех с
минимальным количеством кода. Нам нужно будет хранить цвета вершин. И граф мы
будем строить исходя из того, что дорога типа B прямой путь, а дорога типа R -
обратный. Таким образом решение будет завязано на поиск цикла. Как только при
обходе мы натыкаемся на "серый" цвет, значит мы нашли путь в вершину с другим
типом дороге и тут же можно прекратить выполнение программы, так как граф уже
не оптимален. Я реализовал выход через raise, создал свой класс NotOptimised
унаследованный от Exception, для лучшего понимания кода.
P.S.: на текущий момент, могу сказать, что данная задача одна из самых
сложных  на курсе, не знаю, что там будет дальше, но над ней я просидел почти
3 недели..
-------------------------------------------------------------------------------
Сложность:
Временная DFS - O(V + E), V - кол-во вершин, E - кол-во ребер.
Пространственная сложность - дополнительно выделяется память под массив цветов
размером равным количеству вершин - O(V), а также нам нужна память под стек
вершин при обходе DFS - O(V).
-------------------------------------------------------------------------------
Данные посылки:
1.009s 48.26Mb
-------------------------------------------------------------------------------
"""

from typing import List, Tuple, NoReturn
from collections import defaultdict


class NotOptimised(Exception):
    pass


class Graph:
    def __init__(self, n: int):
        self.size = n
        self.edges = defaultdict(list)
        self.color = ['white'] * (self.size + 1)

    def add_edge(self, v: int, u: int) -> NoReturn:
        self.edges[v].append(u)

    def dfs(self, start_vertex: int) -> NoReturn:
        stack: List[int] = list()
        stack.append(start_vertex)
        while len(stack) > 0:
            v = stack.pop()
            if self.color[v] == 'white':
                self.color[v] = 'gray'
                stack.append(v)
                for u in self.edges[v]:
                    if self.color[u] == 'white':
                        stack.append(u)
                    if self.color[u] == 'gray':
                        raise NotOptimised()
            elif self.color[v] == 'gray':
                self.color[v] = 'black'


def solution(n: int, rails: List[Tuple[str]]) -> NoReturn:
    graph = Graph(n)
    for i, road in enumerate(rails, start=1):
        for j, type_road in enumerate(road, start=1):
            if type_road == 'B':
                graph.add_edge(i, i + j)
            else:
                graph.add_edge(i + j, i)
    try:
        for start in range(1, n + 1):
            if graph.color[start] == 'white':
                graph.dfs(start)
        print("YES")
    except NotOptimised:
        print("NO")


def input_data():
    n = int(input())
    rails = []
    m = n - 1
    while m:
        rails.append((input().strip()))
        m -= 1
    return n, rails


if __name__ == '__main__':
    solution(*input_data())

"""
3
RB
R

4
BBB
RB
B

5
RRRB
BRR
BR
R

10
RRBRRBRRR
BBBBBBRB
BBRBRRR
RRBRRR
RBRRR
BBRR
RRR
RR
B

"""
