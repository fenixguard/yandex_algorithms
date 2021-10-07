def get_longest_word(line: str) -> str:
    words_list = line.lstrip().rstrip().split(' ')
    big_word = ''
    for word in words_list:
        if len(word) > len(big_word):
            big_word = word

    return big_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
