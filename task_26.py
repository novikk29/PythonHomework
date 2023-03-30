# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os
os.system('clear')
def exponentiation(numA, numB): 
    if numB == 0: 
        return 1
    return (numA *exponentiation(numA, numB - 1))
numA = int(input("Введите число A: "))
numB = int(input("Введите число B: "))
result = exponentiation(numA, numB) 
print()
print(f"{numA} в степени {numB} равно {result}")
print()