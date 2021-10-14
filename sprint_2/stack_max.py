from typing import List, Tuple, NoReturn


class StackMax:
    _stack = []
    _max_element = None

    def size(self):
        if len(self._stack) > 0:
            return 1
        else:
            return 0

    def set_max_element(self, element):
        if self._max_element is not None:
            if self._max_element < element:
                self._max_element = element
        else:
            self._max_element = element

    def push(self, element):
        self._stack.append(element)
        self.set_max_element(element)

    def pop(self):
        if self.size():
            element = self._stack.pop()
            if self.size():
                if element == self._max_element:
                    self._max_element = max(self._stack)
            else:
                self._max_element = None
        else:
            print('error')

    def get_max(self):
        if len(self._stack) == 0:
            print('None')
        else:
            print(self._max_element)


def solution(command_list: List[Tuple[str, str]]) -> NoReturn:
    stack = StackMax()
    for command in command_list:
        if command[0] == 'get_max':
            stack.get_max()
        elif command[0] == 'push':
            stack.push(int(command[1]))
        else:
            stack.pop()


def input_data() -> List[Tuple]:
    n = int(input())
    command_list = []
    while n:
        command = tuple(input().strip().split())
        command_list.append(command)
        n -= 1

    return command_list


if __name__ == '__main__':
    solution(input_data())
