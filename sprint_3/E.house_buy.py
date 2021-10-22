def solution(n: int, k: int, houses: list):
    prefix_sum = [0]
    houses.sort()
    for i, house in enumerate(houses):
        cost = prefix_sum[i] + house
        if cost > k:
            return i
        prefix_sum.append(prefix_sum[i] + house)
    return n


def input_data():
    n, k = map(int, input().strip().split())
    houses = list(map(int, input().strip().split()))
    return n, k, houses


if __name__ == '__main__':
    print(solution(*input_data()))
