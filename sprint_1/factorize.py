from typing import List


def factorize(number: int) -> List[int]:
    devisors = []
    div = 2
    while number >= div * div:
        while number % div == 0:
            devisors.append(div)
            number //= div
        div += 1

    if number > 1:
        devisors.append(number)

    return devisors


result = factorize(int(input()))
print(" ".join(map(str, result)))
