"""
Привет! ID успешной посылки: 54853357
_____________________________________
Задача:
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x),
push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала
очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации нельзя использовать связный список.
____________________________________________________________
Так как связный список использовать нельзя, я подумал и пришел к тому, что самое оптимальное решение это использовать
два массива, НО потом мне подсказали и я подумал еще получше - циклический буфер будет лучшим выбором!
Будем использовать для метода push_back и push_front для вставки значений в конец и начало буфера.
Также мы заведем в классе Deque поле size, в котором будем хранить максимальный размер Дека, задаваемый во входных
данных. Поля tail и head для хранения индексов хвоста буфера и начала. Поле count - хранение количества элементов в
буфере. Ну и соответственно проинициализируем саму очередь на заданный размер.
Идея алгоритма простая, мы считываем данные, упаковываем их в массив, далее через оператов if - elif на нужные команды
вызываем нужные методы.

Для реализации алгоритма нам нужен класс, в котором будет реализованы следующие методы:
 * push_back(value) - добавляет элемент в конец буфера
 * push_front(value) - добавляем элемент в начало буфера
 * pop_back() - удаляет элемент из конца буфера
 * pop_front() - удаляет элемент из начала буфера
Два дополнительный метода is_full() и is_empty() позволят нам отлавливать моменты, когда дека заполнена или пуста, и
выкидывать в методах добавления и удаления элементом исключения, которые мы будем обрабатывать снаружи.
При добавление в конец проверяем, что буфер не заполнен, далее проверяем, что элементы в буфере уже есть, проверяем
если tail + 1 == size, то обнуляем tail, в противном случае увеличиваем tail на 1, для того, чтобы не перезатереть
значение, которое уже лежит в буфере. Если буфер пустой, то tail и  head обнуляем и записываем по индексу tail значение
value. Увеличиваем счетчик элементов буфере на 1.
Аналогичная ситуация для добавления в начало. Только здесь необходимо следить за индексом в head для того, чтобы не
перезатереть значение, которое уже записано в буфер. Добавление происходит по индексу head, и увеличение счетчика на 1.
Далее методы удаления элементов.
Удаление с конца. Проверяем буфер на пустоту. Сохраняем текущий индекс в idx из tail во временную переменную именно по
этому индексу мы и извлечем значение. Далее нам нужно переопределить индексы в tail и head, чтобы они указывали на
правильные позиции буфера после удаления элемента. Уменьшаем счетчик на 1. Берем элемент по индексу idx из буфера, а на
его место записываем None. Удалять элементы нельзя, чтобы не изменился размер буфера. По идее элементы можно не заменять
на None, а просто сдвигать tail и head на нужные новые позиции и уменьшать счетчик. Но в задании указано удалить и мы
его удаляем.
Удаление с начала аналогичное. В idx сохраняем индекс из head, далее переопределяем tail и head для новых позиций,
уменьшаем счетчик на 1 и возвращаем элемент.
------------------------------------------------------------
Про сложность.
Алгоритм выполняется за линейное время O(n), где n - количество команд.
Сами операции выполняются за O(1).
Мы тратим на работу алгоритма O(n) памяти, потому что длина буфера не превосходят 0 <= n <= 50_000,
где n это маскимальный размер Дека.
------------------------------------------------------------
Данные посылки:
0.56s 19.71Mb

"""

from typing import List, Tuple, NoReturn


class Deque:

    def __init__(self, n: int):
        self.queue = [None] * n
        self.head = 0
        self.tail = 0
        self.size = n
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def push_back(self, value):
        if self.is_full():
            raise IndexError()
        if self.count:
            if self.tail + 1 == self.size:
                self.tail = 0
            else:
                self.tail += 1
        else:
            self.tail = self.head = 0

        self.queue[self.tail] = value
        self.count += 1

    def push_front(self, value: int):
        if self.is_full():
            raise IndexError()
        if self.count:
            if self.head - 1 < 0:
                self.head = self.size - 1
            else:
                self.head -= 1
        else:
            self.tail = self.head = 0

        self.queue[self.head] = value
        self.count += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError()
        idx = self.tail
        if self.count == 1:
            self.tail = self.head = -1
        else:
            if self.tail - 1 < 0:
                self.tail = self.size - 1
            else:
                self.tail -= 1
        self.count -= 1
        item = self.queue[idx]
        self.queue[idx] = None
        return item

    def pop_front(self):
        if self.is_empty():
            raise IndexError()
        idx = self.head
        if self.count == 1:
            self.tail = self.head = -1
        else:
            if self.head + 1 == self.size:
                self.head = 0
            else:
                self.head += 1
        self.count -= 1
        item = self.queue[idx]
        self.queue[idx] = None
        return item


def input_data() -> Tuple[int, List[Tuple[str, ...]]]:
    n = int(input().strip())
    m = int(input().strip())
    command_list = []
    while n:
        command = tuple(input().strip().split())
        command_list.append(command)
        n -= 1
    return m, command_list


def solution(deque_length: int, command_list: List[Tuple[str, ...]]) -> NoReturn:
    deque = Deque(deque_length)
    for command in command_list:
        if command[0] == 'push_back':
            try:
                deque.push_back(int(command[1]))
            except IndexError:
                print('error')
        elif command[0] == 'push_front':
            try:
                deque.push_front(int(command[1]))
            except IndexError:
                print('error')
        elif command[0] == 'pop_back':
            try:
                print(deque.pop_back())
            except IndexError:
                print('error')
        elif command[0] == 'pop_front':
            try:
                print(deque.pop_front())
            except IndexError:
                print('error')


if __name__ == '__main__':
    solution(*input_data())
