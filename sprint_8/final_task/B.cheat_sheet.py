"""
ID успешной посылки: 64870467
-------------------------------------------------------------------------------
Задача:
Написать программу, которая по длинной строке и набору допустимых слов опре-
делит, можно ли разбить текст на отдельные слова из набора.
Выведите «YES», если текст можно разбить на слова из данного словаря, или «NO»
в ином случае.
-------------------------------------------------------------------------------
Алгоритм:
Для начала создадим префиксное дерево на основе допустимых слов. Далее процесс
начинаем с корня бора. Перебираем символы шаблона, начиная со стартовой позиции.
Берем символ, если он есть в текущем узле, то смещаемся в следующий узел. Если
следующий узел оказался терминальным, то отмечаем позицию как достижимую.
Если же символа нет, получается что подходящего ребра нет, продолжаем обработку
перейдя к следующему символу строки. Результат будет лежать в конце массива
valid. Его мы и возвращаем. Если добрались до конца, значит строку можно
разбить, в противном случае - нет.
-------------------------------------------------------------------------------
Сложность:
Временная сложность - O(L) тратится на построение бора, где L - суммарная длина
слов в множестве. O(n*M) - тратится на нахождение разбиения, где n - длина
текста, M - длина самого длинного шаблона. Итоговая сложность O(L) + O(n*M).
Пространственная сложность - O(L) исползуется для хранения дерева, где L -
суммарная длина слов в множестве. O(K) на массив терминальных элементов, где
K - количество элементов в префиксном дереве. O(n) - на хранение достижимых
позиций, где n - длина строки из входных данных задания. Итогая сложность
O(L+K+n)
-------------------------------------------------------------------------------
Данные посылки:
208ms 5.93Mb
"""

from typing import List, Tuple, NoReturn


class TrieNode:

    def __init__(self):
        self.terminals = [False]
        self.trie = [{}]

    def add_word(self, word: str) -> NoReturn:
        current_node = self.trie[0]
        current_node_index = 0

        for char in word:
            if char not in current_node:
                current_node[char] = len(self.trie)
                self.trie.append({})
                self.terminals.append(False)

            next_node_index = current_node[char]
            current_node = self.trie[next_node_index]
            current_node_index = next_node_index

        self.terminals[current_node_index] = True


def solution(input_string: str, words: List[str]) -> bool:
    tr = TrieNode()
    for word in words:
        tr.add_word(word)

    valid = [True] + [False] * len(input_string)

    for pos in range(len(input_string)):
        if not valid[pos]:
            continue

        current_node = tr.trie[0]
        offset = 0
        mismatch_not_found = True

        while mismatch_not_found and pos + offset < len(input_string):
            symbol = input_string[pos + offset]

            if symbol in current_node:
                next_index = current_node[symbol]
                current_node = tr.trie[next_index]
                if tr.terminals[next_index]:
                    valid[pos + offset + 1] = True
                offset += 1
            else:
                mismatch_not_found = False

    return valid[len(input_string)]


def input_data() -> Tuple[str, List[str]]:
    input_string = input().strip()
    n = int(input().strip())
    words = list()
    for _ in range(n):
        words.append(input().strip())

    return input_string, words


if __name__ == '__main__':
    answer = solution(*input_data())
    if answer:
        print("YES")
    else:
        print("NO")
