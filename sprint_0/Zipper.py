n = int(input())

array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

new_array = list()

for i in range(n):
    new_array.append(array_1[i])
    new_array.append(array_2[i])

print(" ".join(list(map(str, new_array))))
