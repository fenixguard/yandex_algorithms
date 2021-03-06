"""
ID удачной посылки: 57490557
------------------------------------------------------------------------------------------------------------------------
Задание
------------------------------------------------------------------------------------------------------------------------
Написать поисковую систему.
Имеется n документов, каждый из которых представляет осбой текст из слов. По этим документам требуется построить
поисковый индекс. На вход системе будут подаваться запросы. Запрос - некоторый набор слов. По запросу надо вывести 5
самых релеватных документов. Релевантоность документа оценивается следующим образом: для каждого уникального слова из
запроса берётся число его вхождений в документ, полученные числа для всех слов из запроса суммируются. Итоговая сумма
и является релевантностью документа. Сортировка документов на выдаче производится по убыванию релевантности. Если
релевантность совпадает - то по возрастанию их порядковых номеров в базе.
------------------------------------------------------------------------------------------------------------------------
Описание работы алгоритма
------------------------------------------------------------------------------------------------------------------------
В функции input_data считываем данные. Так как каждый документ представляет строку, то сплитим ее по пробелам, создаем
из нее массив, и этот массив добавляем в обший массив документов. Аналогично поступаем с запросами, но так как по
условию задания берется уникальное слово из запроса, то вместо списка мы создаем из слов множество, тем самым отсекаем
повторы, и тоже добавляем в общий массив запросов.
В функции create_search_index создаем поисковый индекс из списка документов. Логика следующая. Бежим по всем документам,
у каждого документа бежим пословам, это слово и будет ключом в хеш-таблице. У данного ключа будет вложенная структура -
словарь, где ключом будет номер документа, а значением - количество вхождений слова в этот документ.
Основная функция solution. Получаем в ней поисковый индекс. Далее бежим по всем запросам, создаем вспомогательный
словарь для подсчета слов внутри запроса. Из запроса берем по очереди слова и проверяем их вхождение в поисковый индекс.
Если вхождение есть, то складываем значения словарей со счетчиками слов. Таким образом в конце прозода по запроса мы
получаем словарь, в котором ключ номер документа, а значение - релевантность. Сортируем, используя лямбда функцию, и
выводим только 5 элементов. И так далее по всем запросам.
------------------------------------------------------------------------------------------------------------------------
Сложность
------------------------------------------------------------------------------------------------------------------------
Временная:
---------------------------------
Разобьем на два этапа.
1. Построение поискового индекса:
O(n*w1) - мы проходим по всем документам, а внутри по всем словам документа (n - количество документов, w1 - среднее
количество слов в документе).
Операция вставки в словарь имеет в среднем сложность O(1) - ее мы опускаем, так как она сильно меньше O(n^2)/
2. Поиск релевантных документов:
Аналогичная ситуация с построением структуры для подсчета релевантных документов. O(m*w2) - где m - количество запросов,
w1 - среднее количество слов в запросе.
Также мы сортируем эту структура используя встроенную функцию sorted(), которая основана на алгоритме Timsort, отсюда
худшая сложность будет O(k*log(k)), в лучшем O(k), где k - количество элементов структуры содержащей релевантные
элементы.
---------------------------------
Пространственная:
---------------------------------
Разобьем подсчет на два этапа.
1. Поисковый индекс:
O(n), где n - количество всех слов во всех документах.
2. Поиск релевантных документов:
O(k), где k - количество документов подходящих под запрос на каждом этапе.
Дополнительно - O(w2), где w2 - среднее количество слов в запросе, мы делаем из листа сет, а также O(k) - для выдачи
результата, где k - количество документов подходящих под запрос, так как функция sorted() возвращает аналогичной длины
структуру, которая была подана на вход, только в отсортированном порядке.
------------------------------------------------------------------------------------------------------------------------
Данные посылки
------------------------------------------------------------------------------------------------------------------------
4.684s 55.32Mb
------------------------------------------------------------------------------------------------------------------------
"""

from typing import Tuple, List, Dict
from collections import Counter, defaultdict


def solution(documents: List[List[str]], queries: List[List[str]]):
    search_index = create_search_index(documents)

    for query in queries:
        counter_docs = dict()
        for word in set(query):
            docs = search_index.get(word)
            if docs:
                if len(counter_docs):
                    counter_docs = Counter(counter_docs) + Counter(docs)
                else:
                    counter_docs = docs
        print(*[k for k, _ in sorted(counter_docs.items(), key=lambda x: (-x[1], x[0]))][:5])


def create_search_index(docs: List[List[str]]) -> Dict[str, Dict[int, int]]:
    search_index = defaultdict(dict)
    for doc_id, document in enumerate(docs, start=1):
        for word in document:
            search_index[word][doc_id] = search_index[word].get(doc_id, 0) + 1
    return search_index


def input_data() -> Tuple[List[List[str]], List[List[str]]]:
    n = int(input())
    docs = list()
    while n:
        docs.append(input().strip().split())
        n -= 1
    m = int(input())
    reqs = list()
    while m:
        reqs.append(input().strip().split())
        m -= 1

    return docs, reqs


if __name__ == '__main__':
    solution(*input_data())
