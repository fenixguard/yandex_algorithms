"""
ID успешной посылки:
-------------------------------------------------------------------------------
Задача:
Выведите наибольший общий префикс распакованных строк.
-------------------------------------------------------------------------------
Алгоритм:
Сначала распаковываем строку посимвольно считывая ее, если строка требует распа-
ковки, то делаем ее рекурсивно считая правильную последовательность скобок.
Далее находим общий префикс путем посимвольного сравнения каждого символа
строки с другим символом на этой позиции, а найдя длину - выводим сам префикс.
Чтобы оптимизировать этап распаковки добавил кэш.
-------------------------------------------------------------------------------
Сложность:
Временная сложность - O (m*n + m*n*k), где первое слагаемое отвечает за слож-
ность поиска общего префикса, а второе слагаемое - распаковка строки
(m - длина строки, n - количество строк, k - количество вложенностей выражения)
Пространственная сложность - O(1) для поиска префикса и  O(m*n) для распаковки,
где n - длина строки, m - количество строк.
-------------------------------------------------------------------------------
Данные посылки:

"""
from string import digits
from typing import List

cache_dict = dict()


def unpack_string(cur_string: str, multiplier: int = 1) -> str:
    if cache_dict.get(cur_string) is not None:
        return cache_dict[cur_string] * multiplier

    chunks = []
    string_length = len(cur_string)

    if string_length == 0:
        cache_dict[cur_string] = ''
        return cache_dict[cur_string]

    mul = ""
    opened = 0
    flushed = True
    start = 0
    end = 0
    for i in range(string_length):
        char = cur_string[i]

        if char in digits and not opened:
            mul += char
            continue

        if char == "[":
            if not opened:
                if end > start:
                    chunks.append(cur_string[start:end])
                opened += 1
                flushed = True
                start = i
                continue

            opened += 1
            continue

        if char == "]":
            if opened == 1:
                end = i
                opened = False
                if end - start > 1:
                    chunks.append(unpack_string(cur_string[start + 1:end], int(mul if len(mul) > 0 else "1")))

                mul = ''
                flushed = True
                start = i + 1
                continue

            opened -= 1
            continue

        flushed = False
        end = i + 1

    if not flushed and start < end:
        chunks.append(cur_string[start:end])

    cache_dict[cur_string] = "".join(chunks)

    return cache_dict[cur_string] * multiplier


def solution(strings: List[str]) -> str:
    prefix = 0

    min_length = 10 ** 5 + 1  # по условию
    max_length = 0

    for i in range(len(strings)):
        if len(strings[i]) > max_length:
            max_length = len(strings[i])

        if len(strings[i]) < min_length:
            min_length = len(strings[i])

    if min_length * max_length == 0:
        return ""

    if len(strings) == 0:
        return ""

    for i in range(max_length):
        try:
            char = None
            match = True
            for s in strings:
                if char is None:
                    char = s[i]

                if char != s[i]:
                    match = False
                    break

            if match:
                prefix += 1
                continue

            break
        except IndexError:
            break

    return strings[0][:prefix]


def input_data() -> List[str]:
    n = int(input().strip())
    unpacked = [""] * n
    for i in range(n):
        packed = input().strip()
        unpacked[i] = unpack_string(packed)

    return unpacked


if __name__ == '__main__':
    print(solution(input_data()))
