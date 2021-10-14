class BracketStack:
    _stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1]

    def size(self):
        return len(self._stack)


def is_correct_bracket_seq(sequence: str) -> bool:
    if len(sequence) == 0:
        return True

    bracket_stack = BracketStack()
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    for s in sequence:
        if s in brackets.keys():
            bracket_stack.push(s)
        else:  # Если закрывающиеся
            if bracket_stack.size() == 0:
                return False
            top_item = bracket_stack.top()
            if brackets.get(top_item) == s:
                bracket_stack.pop()
            else:
                return False
    if bracket_stack.size() == 0:
        return True
    else:
        return False


def input_data() -> str:
    return input().rstrip()


if __name__ == '__main__':
    print(is_correct_bracket_seq(input_data()))
