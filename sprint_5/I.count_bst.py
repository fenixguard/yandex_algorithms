
def solution():
    n = int(input())
    gn = [0] * (n + 1)
    gn[0] = 1
    gn[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            gn[i] += gn[j - 1] * gn[i - j]
    print(gn[-1])


if __name__ == '__main__':
    solution()
