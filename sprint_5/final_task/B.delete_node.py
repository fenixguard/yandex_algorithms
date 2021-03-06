"""
ID успешной посылки: 59099806
-------------------------------------------------------------------------------
Задача:
Дано BST, в котором хранятся ключи. Найти вершину с заданным ключом и удалить
её из дерева, так чтобы дерево осталось корректным BST
-------------------------------------------------------------------------------
Алгоритм:
Есть три рассматриваемых случая. Удаляемый элемент может находиться в корне, в
левом поддереве, в правом поддереве. Отсюда следует несколько условий решения.
Если исходное дерево None, то на вход пришло пустое дерево и мы вовзращаем его.
Если ключ меньше ключа вершины, тогда искомый элемент в левом поддереве и мы
запускаем рекурсивно поиск с удалением ключа на левом поддереве. Если ключ
оказался больше ключа вершины, то аналогично поступаем, но уже с правым под-
деревом.
Мы нашли удаляемый ключ. Теперь необходимо проверить, есть ли у него потомки.
В зависимости от количества потомков 0, 1 или 2, алгоритм будет отличаться.
Если потомков 2, то мы удаляем элемент, а ему на замену ищем элемент в правом
поддереве родителя, углубляясь в левую ветку. Так как там по определению самое
маленькое значение из правого поддерева, и оно точно не меньше, чем любое
значение левого поддерева (функция min_value_node). После того, как мы пере-
несли значение снизу вверз, нам надо его удалить внизу, запускаем рекурсивно
поиск ключа на правом поддереве и удаляем его. Так как этот элемент был после-
дним в дереве, то ему замену искать не нужно, и дерево не распадется. Его
можно спокойно удалить.
-------------------------------------------------------------------------------
Сложность:
Данный алгоритм работает за O(h), где h - глубина (высота) дерева.
Дополнительной памяти потребуется O(k), где k - размер стека вызова, k пропор-
ционально высоте дерева h.
-------------------------------------------------------------------------------
Данные посылки: 1.351s 29.02Mb
-------------------------------------------------------------------------------
"""


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(root, key: int):
    if root is None:
        return root
    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = min_value_node(root.right)

        root.value = temp.value
        root.right = remove(root.right, temp.value)
    return root
