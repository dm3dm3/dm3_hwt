# coding : utf-8
# PEP-8
# Python-1-lesson5-easy Task 1
# под Python3 - в частности Python 3.7.2

import sys
import os
import mydirfunctions as dirfuncs #сделать надо родительскую директорию читаемой по-умолчанию, например Sources_Root


def start_util():
    """Ф-ия запуска консольной утилиты"""
    option = {
        "help": dirfuncs.print_help,
        "mkdir": dirfuncs.mkdir_name,
        "rmdir": dirfuncs.rmdir_name,
        "chdir": dirfuncs.cd_name,
        "ldir": dirfuncs.list_all
    }
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None
    try:
        key = sys.argv[1]
    except IndexError:
        key = None
    if key:
        if option.get(key):
            option[key](dir_name)
        else:
            print('Неверный параметр. Смотрите HELP - ключ help -  для получения справки')
            dirfuncs.print_help()
    else:
        print('Ключ не задан. Смотрите HELP - ключ help -  для получения справки')
        dirfuncs.print_help()


print('МОЯ УТИЛИТА ЗАПУЩЕНА>>> ')
print(f'>>{os.getcwd()} >>>\n')
start_util()
print('\nМОЯ УТИЛИТА ОСТАНОВЛЕНА>>> ')


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
