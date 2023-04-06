# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
import os
os.system('clear')


def fillArray(arraySize):
    return [randint(1, 10) for _ in range(arraySize)]


def searchIndex(array_1, min_num, max_num):
    return [i for i, num in enumerate(array_1) if min_num <= num <= max_num]
    # arr = []
    # for i, num in enumerate(array_1):
    #     if min_num <= num <= max_num:
    #         arr.append(i)
    # return arr


array_1 = fillArray(int(input('введите количество элементов массива: ')))
min_num = int(input('введите минимальное значение диапазона: '))
max_num = int(input('введите максимальное значение диапазона: '))
print(array_1)
print(searchIndex(array_1))
