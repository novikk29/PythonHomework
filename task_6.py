# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

k = input('введите шестизначное число: ')
a = int(k[0])
b = int(k[1])
c = int(k[2])
d = int(k[3])
e = int(k[4])
f = int(k[5])
s1 = a + b + c
s2 = d + e + f
if s1 == s2:
    print('yes')
else:
    print('no')