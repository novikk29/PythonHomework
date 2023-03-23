# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint
n = int(input("Введите количество элементов: "))
x = int(input("Введите искомое число: "))
counter = 0
list_1 = [randint(1, 100) for _ in range(n)]
print(list_1)
for i in list_1:
    if i == x:
        counter += 1
print(f'число {x} встречается в массиве {counter} раз(а)')
list2 = list_1.copy()
counter2 = 0
x_str = str(x)
for num in list2:
    num_str = str(num)
    if x_str in num_str:
        for elem in num_str:
            if x_str == elem:
                counter2 += 1
print(f"Цифра {x} встречается в массиве {counter2} раз(а)")
