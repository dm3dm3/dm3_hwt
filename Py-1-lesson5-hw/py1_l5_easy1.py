# coding : utf-8
# PEP-8
# Python-1-lesson5-easy Task 1

import sys
import os

def mkdir_proc(start, stop):
    """Ф-ия создания директорий"""
    for indx in range(start,stop+1):
        new_dir = os.path.join(os.getcwd(), f'dir_{indx}')
        try:
            os.mkdir(new_dir)
            print('папка {} создана'.format(f'dir_{indx}'))
        except FileExistsError:
            print('папка {} уже существует'.format(f'dir_{indx}'))


def rmdir_proc(start, stop):
    """Ф-ия удаления директорий"""
    for indx in range(start,stop+1):
        used_dir = os.path.join(os.getcwd(), f'dir_{indx}')
        try:
            os.rmdir(used_dir)
            print('папка {} удалена'.format(f'dir_{indx}'))
        except FileNotFoundError:
            print('папка {} отсутствует'.format(f'dir_{indx}'))

num_start = 1
num_finish = 9
print('создаём {} папок'.format(num_finish-num_start+1))
mkdir_proc(num_start,num_finish)
input('\tДля продолжения нажмите ENTER.')
print('удаляем {} папок'.format(num_finish-num_start+1))
rmdir_proc(num_start,num_finish)


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
