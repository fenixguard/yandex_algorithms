"""
ID успешного решения: 54320357

Замечания по условию задачи.
По условию задания нужно было обратить внимание на несколько моментов. Во-первых, длина входного массива - до 1 млн
значений. Во-вторых, сами значения массива до 10^9. Исходя из этих данных ввод я решил сделать из файла, так как это
быстрее, чем считывание из консоли. Также стоит отметить ограничение во времени 3 секунды для python. Отсюда можно
понять, что алгоритм со сложностью больше линейной нам не подойдет. С учетом, что python сможет совершить в лучшем
случае 100млн операций за секунду, то квадратичный алгоритм уйдет далеко за 3 секунды с длиной массива в 1 млн значений.

Прицнип работы.
Фукнция read_input считывает входные данные и передает их в функцию nearest_null.
Идея алгоритма заключается в том, пройти массив слева направо проставить дистации, а потом справа налево и дозаполнить
массив.
Заводим результирующий массив result_dist длины n и заполняем его нулями.

Алгоритм следующий. Идем по массиву вправо. До встречи первого нуля заполняем массив большим значением, например длиной
массива. При встрече первого нуля в результирующий массив проставляем ноль и обновляем флаг нуля. Далее если нам
встречаются значния отличные от нуля, то в результирующий массив добавляем значение предыдущей ячейки результата плюс 1.
Таким образом проходим до конца. Начинаем движение обратно. До встречи первого нуля ничего не меняем в массиве. При
встрече нуля обновляем флаг нуля, далее все значения отличные от нуля записываем в массив по правилу: берется
минимальное значение из текущего значения и следующего плюс 1

Вывод.
Таким образом у нас получается сложность O(n), где n - длина входного массива. Вложенные циклы отсутствуют.
Результаты записываются в выходной файл, для того, чтобы не тратить дополнительное время на принты в консоль.
1.576s 113.63Mb

"""
from typing import List, Tuple, NoReturn


def nearest_null(n: int, sequence: List[int]) -> List[int]:
    result_dist = [0] * n
    length_sequence = len(sequence)

    zero_flag = False
    for i in range(length_sequence):  # Проход вправо ->
        if sequence[i] == 0:
            zero_flag = True
            result_dist[i] = 0

        else:  # sequence[i] =! 0
            if zero_flag:
                result_dist[i] = result_dist[i - 1] + 1
            else:
                result_dist[i] = length_sequence

    zero_flag = False
    for i in reversed(range(length_sequence)):  # Проход влево <-
        if sequence[i] == 0:
            zero_flag = True
            result_dist[i] = 0

        else:  # sequence[i] =! 0
            if zero_flag:
                result_dist[i] = min(result_dist[i], result_dist[i + 1] + 1)

    return result_dist


def read_input() -> Tuple[int, List[int]]:
    with open('input.txt') as input_file:
        n = int(input_file.readline().strip())
        sequence = list(map(int, input_file.readline().strip().split()))

    return n, sequence


def write_result(result: List[int]) -> NoReturn:
    with open('output.txt', 'w') as out_file:
        out_file.write(" ".join(map(str, result)))


if __name__ == '__main__':
    result = nearest_null(*read_input())
    write_result(result)
