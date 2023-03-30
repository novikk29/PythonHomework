# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
# чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя
# использовать циклы.
# 2 2
# 4

import os
os.system('clear')
def NumbersSum(numberA, numberB): 
    if (numberA == 0): 
        return numberB 
    elif (numberB == 0): 
        return numberA 
    else: 
        return NumbersSum(numberA-1, numberB+1)
numberA = int(input("Введите число A: "))
numberB = int(input("Введите число B: "))
result = NumbersSum(numberA, numberB) 
print()
print(f"Сумма чисел {numberA} и {numberB} равна {result}")
print()
