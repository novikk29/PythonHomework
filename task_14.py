# Задача 14: Требуется вывести все целые степени двойки (т.е. числавида 2k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('введите число n: '))
k = 0
while k**2 < n:
    print(2**k)
    k += 1