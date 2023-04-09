from logger import *
import os
os.system('clear')

def interface():
    print("""1 - записать данные
2 - вывести данные
3 - поиск 
4 - импорт в файл
5 - измененние данных
6 - удаление данных""")
    var = input("введите номер варианта: ")
    while var not in ("1","2","3","4","5","6"):
        os.system('clear')
        print("такой команды не существует")
        print("""1 - записать данные
2 - вывести данные
3 - поиск 
4 - импорт в файл
5 - измененние данных
6 - удаление данных""")
        var = input("введите число от 1 до 6: ")
    if var == "1":
        input_data()
    elif var == "2":
        print_data()
    elif var == "3":
        search()
    elif var == "4":
        load()
    elif var == "5":
        change()
    elif var == "6":
        delete()
    