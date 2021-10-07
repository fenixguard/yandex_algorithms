def check_parity(a: int, b: int, c: int) -> bool:
    tail = []
    if a % 2 != 0:
        tail.append(a)
    if b % 2 != 0:
        tail.append(b)
    if c % 2 != 0:
        tail.append(c)

    if len(tail) == 0 or len(tail) == 3:
        return True
    else:
        return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
