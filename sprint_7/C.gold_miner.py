

def solution():
    m = int(input())
    n = int(input())
    bag = [None for _ in range(n)]
    for i in range(n):
        bag[i] = tuple(map(int, input().strip().split()))

    total_cost = 0
    for b in sorted(bag, reverse=True):
        cost = b[1] if b[1] <= m else m
        m -= cost
        total_cost += b[0] * cost

        if m == 0:
            break

    print(total_cost)


if __name__ == '__main__':
    solution()

