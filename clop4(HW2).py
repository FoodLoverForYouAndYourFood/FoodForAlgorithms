"""
Сложность алгоритма O(n). Если удовлетворяет условию кидаем в макс, если меньше чем предыдущий то в мин
"""


def clop4k(arr):
    profitforus = 0
    min = 0
    max = 0
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            min = arr[i - 1]
        else:
            if max < arr[i - 1]:
                max = arr[i - 1]
        if max != 0 and min != 0:
            profitforus += max - min
            max = 0
            min = 0
    if max == 0:   
        max = arr[-1]
        profitforus += max - min
    return profitforus


print(clop4k([7,6,4,3,1]))
