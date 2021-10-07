def to_binary(number: int) -> str:
    bin_number = []
    while number > 1:
        bin_number.append(number % 2)
        number //= 2
    bin_number.append(number)
    return ''.join(map(str, bin_number))[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
