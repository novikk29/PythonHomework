
from data_create import *


def input_data():
    lastname = lastname_data()
    name = name_data()
    phonenum = phone_data()
    with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "a", encoding="utf-8") as file:
        file.write(f"{lastname}    {name}    {phonenum}\n")


def print_data():
    with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "r", encoding="utf-8") as data:
        data_first = data.read()
        print(data_first)
    return data_first


def search():
    lookfor = input("кого ищем? ")
    with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)


def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_second.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")


def change():
    line_str = input("Введите запись, которую нужно изменить: ")
    with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if line_str not in line:
                    data_1.write(line)
                else:
                    print()
                    print(line)
                    ask_1 = input("Изменить эту строку? (да, нет): ")
                    while ask_1 not in ("да", "нет"):
                        print("ввод некорректный")
                        ask_1 = input("Изменить эту строку? (да, нет): ")
                    if ask_1 == "да":
                        ask = input("Что хотите поменять? (1, 2, 3): ")
                        while ask not in ("1", "2", "3"):
                            print("ввод некорректный")
                            ask = input("Что хотите поменять? (1, 2, 3): ")
                        new_data = input("введите новые данные: ")
                        line_list = line.split()
                        line_list[int(ask) - 1] = new_data
                        data_1.write("\t".join(line_list) + "\t" + "\n")
                    elif ask_1 == "нет":
                        data_1.write(line)


def delete():
    line_str = input("Ведите запись, которую нужно удалить: ")
    with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("/Users/novikk-mac/Documents/тестировщик/python/homework/task_38/data_first.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if line_str not in line:
                    data_1.write(line)
                else:
                    print()
                    print(line)
                    ask = input("Удалить эту строку? (да, нет): ")
                    while ask not in ("да", "нет"):
                        print("ввод некорректный")
                        ask = input("Удалить эту строку? (да, нет): ")
                    if ask == "нет":
                        data_1.write(line)
