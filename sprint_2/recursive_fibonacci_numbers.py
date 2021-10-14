
def factorize(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return factorize(n - 1) + factorize(n - 2)


def input_data() -> int:
    return int(input())


if __name__ == '__main__':
    print(factorize(input_data()))
