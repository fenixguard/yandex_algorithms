from typing import List, Tuple


def solution(n: int, schedule: List[Tuple[float, float]]):
    schedule = sorted(schedule, key=lambda x: (x[1], x[0]))
    max_events = 0
    events = []
    time = 0.0
    for event in schedule:
        if event[0] >= time:
            time = event[1]
            max_events += 1
            events.append(event)
    print(max_events)
    for event in events:
        print(f"{event[0]:g} {event[1]:g}")


def input_data():
    n = int(input())
    schedule = [None] * n
    for i in range(n):
        begin, end = map(float, input().strip().split(" "))
        schedule[i] = (begin, end)

    return n, schedule


if __name__ == '__main__':
    solution(*input_data())

"""
5
9 10
9.3 10.3
10 11
10.3 11.3
11 12

3
9 10
11 12.25
12.15 13.3

7
19 19
7 14
12 14
8 22
22 23
5 21
9 23

"""
