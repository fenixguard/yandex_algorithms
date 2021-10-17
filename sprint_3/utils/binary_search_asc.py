def binary_search(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального
        # значит следует искать в левой половине
        return binary_search(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binary_search(arr, x, mid + 1, right)

# изначально мы запускаем двоичный поиск на всей длине массива
# index = binary_search(arr, x, left=0, right=len(arr))
