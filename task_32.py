# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import os
os.system('clear')
from random import randint

def fillArray(arraySize):
    return [randint(1, 10) for _ in range(arraySize)]

def searchIndex(array):
    arr = []
    for i in range(len(array_1)):
        if min_num <= array[i] <= max_num:
            arr.append(i)
    return arr
array_1 = fillArray(int(input('введите количество элементов массива: ')))
min_num = int(input('введите минимальное значение диапазона: '))
max_num = int(input('введите максимальное значение диапазона: '))
print(array_1)
print(searchIndex(array_1))
