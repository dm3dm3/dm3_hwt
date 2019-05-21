# coding : utf-8
# PEP-8
# Python-1-lesson5-easy Task 3

import sys
import os
import shutil


def print_help(*args):
    """Ф-я вывода помощи пользователю"""
    print('\t HELP')
    print("help - получение этой справки")
    print("mkdir <dir_name> - создание поддиректории по текущему пути")
    print("rmdir <dir_name> - удаление поддиректории по текущему пути")
    print("chdir <dir_name> - выбор директории")
    print("ldir [f|d] - содержимое текущей директории: файлы|поддиректории только, без параметра все файлы и поддиректории")


def mkdir_name(dir_name):
    """Ф-ия создания папки с заданным именем"""
    while not dir_name or len(dir_name) < 1 or not dir_name.isalnum():
        print("Необходимо указать имя директории дополнительным параметром")
        dir_name = input('Введите имя директории состоящее из латинских букв и/или цифр: ')
    dir_path = os.path.join( os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def rmdir_name(dir_name):
    """Ф-ия удаления папки с заданным именем"""
    while not dir_name or len(dir_name) < 1 or not dir_name.isalnum():
        print("Необходимо указать имя директории дополнительным параметром")
        dir_name = input('Введите имя директории состоящее из латинских букв и/или цифр: ')
    dir_path = os.path.join( os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директория {} отсутствует'.format(dir_name))


def mkdir_range(start, stop):
    """Ф-ия создания директорий"""
    for indx in range(start,stop+1):
        new_dir = os.path.join(os.getcwd(), f'dir_{indx}')
        try:
            os.mkdir(new_dir)
            print('папка {} создана'.format(f'dir_{indx}'))
        except FileExistsError:
            print('папка {} уже существует'.format(f'dir_{indx}'))


def rmdir_list(start, stop):
    """Ф-ия удаления директорий"""
    for indx in range(start,stop+1):
        used_dir = os.path.join(os.getcwd(), f'dir_{indx}')
        try:
            os.rmdir(used_dir)
            print('папка {} удалена'.format(f'dir_{indx}'))
        except FileNotFoundError:
            print('папка {} отсутствует'.format(f'dir_{indx}'))


def dirs_list(current_dir):
    """Ф-ия выводит поддиректории указанной директории"""
    print('директория {} содержит следующие поддиректории:'.format(current_dir))
    count_dirs = 0
    for dir_in in os.listdir(current_dir):
        if os.path.isdir(dir_in):
            print('\t-\\', dir_in)
            count_dirs += 1
    if count_dirs == 0:
        print('\tПодпапок нет.')


def files_list(current_dir):
    """Ф-ия выводит файлы указанной директории"""
    print('директория {} содержит следующие файлы:'.format(current_dir))
    count_dirs = 0
    for dir_in in os.listdir(current_dir):
        if os.path.isfile(dir_in):
            print('\t--', dir_in)
            count_dirs += 1
    if count_dirs == 0:
        print('\t-Файлов нет.')


def list_all(param):
    """Ф-ия выводит поддиректории и файлы указанной директории"""
    if not param:
        dirs_list(os.getcwd())
        files_list(os.getcwd())
    elif param == 'f':
        files_list(os.getcwd())
    elif param == 'd':
        dirs_list(os.getcwd())
    else:
        print('Неверный параметр. Смотрите HELP - ключ help -  для получения справки')
        print_help()


def copy_file(in_file, out_file):
    """Ф-ия выводит поддиректории указанной директории"""
    print('Копирую файл {}.\n Файл {} будет заменён, если уже существует.'.format(in_file, out_file))
    try:
        out_file = shutil.copyfile(in_file, out_file)
        print('копирование в {} прошло успешно'.format(out_file))
    except shutil.SameFileError:
        print('Вы пытались скопировать файл сам в себя!')


def cd_name(dir_name):
    """Ф-ия смены папки папки с заданным именем"""
    while not dir_name or len(dir_name) < 1 or dir_name.isspace():
        print("Необходимо указать имя директории дополнительным параметром")
        dir_name = input('Введите путь к директории состоящее из латинских букв и/или цифр: ')
    #print(os.getcwd())
    try:
        os.chdir(dir_name)
        print('директория cменена успешно \n Вы сейчас в директории:', os.getcwd())
    except FileNotFoundError:
        print('директория {} отсутствует'.format(dir_name))


if __name__ == '__main__':
    print('sys.argv = ', sys.argv)
    print('8-' * 20 + '8')



