def is_power_of_four(number: int) -> bool:
    if number == 0:
        return False

    while number != 1:
        if number % 4 != 0:
            return False
        number /= 4

    return True


print(is_power_of_four(int(input())))
