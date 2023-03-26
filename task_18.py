# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input("Введите количество элементов: "))
x = int(input("Введите число X: "))
print()
list_1 = [randint(1, 5) for _ in range(n)]
print(list_1)
# print()
print('x =', x)
# print()
# list_1 = sorted(list_1)
# for i in list_1:
#     if i <= x: 
#         number = i
#     else:
#         number = i
#         break
# print('самый близкий по величине элемент массива к заданному числу равен', number)
# print()
min_diff = abs(x - list_1[0])
index_min_diff = 0
for num in range(1,len(list_1)):
    if min_diff > abs(x-list_1[num]):
        min_diff = abs(x-list_1[num])
        index_min_diff = num
print(f'На позиции {index_min_diff} в списке находится самый близкий к {x} элемент и он равен {list_1[index_min_diff]}')
    

    
    
    


