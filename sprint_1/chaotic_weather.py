from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    days = len(temperatures)
    if days == 1:
        return 1
    havoc_days = 0
    for d in range(days):
        if d == 0:
            if temperatures[d] > temperatures[d + 1]:
                havoc_days += 1
        elif d == days - 1:
            if temperatures[d - 1] < temperatures[d]:
                havoc_days += 1
        else:
            if temperatures[d - 1] < temperatures[d] > temperatures[d + 1]:
                havoc_days += 1

    return havoc_days


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
