"""
Привет! ID успешной посылки: 54781671
_____________________________________
Задача:
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x),
push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала
очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации нельзя использовать связный список.
____________________________________________________________
Так как связный список использовать нельзя, я подумал и пришел к тому, что самое оптимальное решение это использовать
два массива. Левый и правый, первый использовать для метода push_back, а второй - push_front.
Также мы заведем в классе Deque поле size, в котором будем хранить максимальный размер Дека, задаваемый во входных
данных.
Идея алгоритма простая, мы считываем данные, упаковываем их в массив, далее через оператов if - elif на нужные команды
вызываем нужные методы.
Для реализации алгоритма нам нужен класс, в котором будет реализованы следующие методы:
 * push_back(value) - Добавляет элемент в левый массив
 * push_front(value) - добавляем элемент в правый массив
 * pop_back() - удаляет элемент из левого массива
 * pop_front() - удаляет элемент из правого массива
Логично подумать, что если у нас постоянно добавляются элементы в правый массив, а потом идет удаление из левого, то это
не значит, что в левом массиве нет значений, они есть и эти значения это реверс правого массива. Для реализации этой
механики нам потребуются два вспомогательных метода в классе, обозначим их приватными, чтобы они не 'торчали' наружу.
 * __fill_front()
 * __fill_back()
Эти два метода позволят нам удалять элементы из левого и правого массива, соответственно, элементы, если эти массивы
пустые и добавление было постоянно только в один.
------------------------------------------------------------
Про сложность.
Алгоритм выполняется за линейное время O(n), где n - количество команд.
Сами операции выполняются за O(1).
Мы тратим на работу алгоритма O(n) памяти, потому что длина левого и правого массива не превосходят 0 <= n <= 50_000,
где n это маскимальная длина Дека.
Что касаемо ввода, то памяти O(n), где n - не более 100_000 строк.
------------------------------------------------------------
Данные посылки:
0.527s 19.80Mb

"""


from typing import List, Tuple, NoReturn


class Deque:

    def __init__(self, size: int):
        self.left = []
        self.right = []
        self.size = size

    def push_back(self, value: int):
        if self.size <= (len(self.left) + len(self.right)):
            print('error')
        else:
            self.left.append(value)

    def push_front(self, value: int):
        if self.size <= (len(self.left) + len(self.right)):
            print('error')
        else:
            self.right.append(value)

    def pop_back(self):
        if not self.left:
            self.__fill_back()
            if len(self.left) == 0:
                return 'error'
        return self.left.pop()

    def pop_front(self):
        if not self.right:
            self.__fill_front()
            if len(self.right) == 0:
                return 'error'
        return self.right.pop()

    def __fill_front(self):
        x = len(self.left) // 2
        if x:
            self.right.extend(self.left[0:x])
            self.right.reverse()
            del self.left[0:x]
        else:
            self.right.extend(self.left)
            if len(self.left):
                del self.left[0]

    def __fill_back(self):
        x = len(self.right) // 2
        if x:
            self.left.extend(self.right[0:x])
            self.left.reverse()
            del self.right[0:x]
        else:
            self.left.extend(self.right)
            if len(self.right):
                del self.right[0]


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
    deque = Deque(size=deque_length)
    for command in command_list:
        if command[0] == 'push_back':
            deque.push_back(int(command[1]))
        elif command[0] == 'push_front':
            deque.push_front(int(command[1]))
        elif command[0] == 'pop_back':
            print(deque.pop_back())
        elif command[0] == 'pop_front':
            print(deque.pop_front())


if __name__ == '__main__':
    solution(*input_data())
