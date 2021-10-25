
def solution():
    with open("input.txt") as file:
        for i, line in enumerate(file):
            if i == 0:
                n = int(line.strip())
            elif i == 1:
                m = int(line.strip())
            elif i == 2:
                north = list(map(int, line.strip().split()))
            else:
                south = list(map(int, line.strip().split()))


    result = north + south
    i = j = k = 0
    while i < n and j < m:
        if north[i] < south[j]:
            result[k] = north[i]
            i += 1
        else:
            result[k] = south[j]
            j += 1
        k += 1
    while j < m:
        result[k] = south[j]
        j += 1
        k += 1

    while i < n:
        result[k] = north[i]
        i += 1
        k += 1

    index = (n + m) // 2
    if (n + m) % 2 == 0:
        print(sum(sorted(result)[index - 1:index + 1]) / 2)
    else:
        print(result[index])


if __name__ == '__main__':
    solution()
