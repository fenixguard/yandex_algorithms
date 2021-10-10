"""
ID успешного решения: 54317536
Замечания по условию задачи.
Максимальная длина входного массива 16 значений. Количество раундов не превышает 9.
Ограничение по времени 1 секунда. Жестких ограничений на сложность по условию нет.

Прицнип работы.
Функция read_input получает данные из консоли. Входные данные передаются в функцию sleight_of_hand.
Так как мы часто будем использовать для сравнения количество нажатых кнопок ребятами, лучше вынести это в отдельную
перменную press_buttons. А в переменную max_points будем складывать количество баллов.
Функция get_count_buttons содержит вынесенную логику из фукнции read_input по заполнению словаря-счетчика кнопок в поле.
Алгоритм следующий: берется очередной номер раунда из ключей словаря. Из словаря field_buttons берется значение
по ключу текущего раунда. Если количество значений в словаре оказалось меньше либо равно количество одновременно
нажатых кнопок ребятами, то они получают балл, в противном случае игра продолжается. Пройдя все раунды мы получаем
максимально возможное количество очков, которые ребята смогли бы заработать.

Вывод.
Алгоритм работает за O(n) 1 <= n <= 4 в фукнции read_input
Алгоритм работает за O(n^2) 1 <= n <= 4 в фукнции get_count_buttons (так как входное поле 4х4) внешний цикл по строкам,
внутренний по символам строки, которые преобразуются в числа.
Алгоритм работает за O(n) 1 <= n <= 9 в фукнции sleight_of_hand.

63ms 3.98Mb

"""
from typing import Dict, Tuple, List


def get_count_buttons(buttons: List[str]) -> Dict[int, int]:
    field_buttons = dict()
    for row in buttons:
        for r in row:
            if r.isdigit():
                num = int(r)
                if field_buttons.get(num):
                    field_buttons[num] += 1
                else:
                    field_buttons[num] = 1
    return field_buttons


def sleight_of_hand(k: int, buttons: List[str]) -> int:
    max_points = 0
    press_buttons = k * 2
    field_buttons = get_count_buttons(buttons)
    for button in field_buttons.keys():
        count_button = field_buttons.get(button)
        if count_button <= press_buttons:
            max_points += 1
    return max_points


def read_input() -> Tuple[int, List[str]]:
    k = int(input())
    buttons = list()
    for _ in range(4):
        buttons.append(input().strip())
    return k, buttons


if __name__ == '__main__':
    result = sleight_of_hand(*read_input())
    print(result)
