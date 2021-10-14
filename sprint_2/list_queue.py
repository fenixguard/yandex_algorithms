from typing import List, Tuple, NoReturn


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class Queue:
    _size = 0
    _queue = []

    def get(self):
        if self.size():
            self._size -= 1
            head = self._queue[0].value
            del self._queue[0]
            print(head)
        else:
            print('error')

    def put(self, node):
        if self._size == 0:
            self._size += 1
            node.next_item = None
            self._queue.append(node)
        else:
            self._size += 1
            self._queue[0].next_item = node
            self._queue.append(node)

    def size(self):
        return self._size


def solution(command_list: List[Tuple[str, str]]) -> NoReturn:
    queue = Queue()
    for command in command_list:
        if command[0] == 'get':
            queue.get()
        elif command[0] == 'put':
            value = int(command[1])
            node = Node(value)
            queue.put(node)
        else:
            print(queue.size())


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
