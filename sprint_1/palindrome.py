from string import punctuation, whitespace


def is_palindrome(line: str) -> bool:
    line = line.lower()
    line_length = len(line)
    if line_length == 1:
        return True

    for i in range(0, len(line) // 2):
        if line[i] in punctuation or line[i] in whitespace:
            continue
        else:
            while line[line_length - 1] in punctuation or line[line_length - 1] in whitespace:
                line_length -= 1
            if line[i] != line[line_length - 1]:
                return False
            line_length -= 1

    return True


print(is_palindrome(input().strip()))
