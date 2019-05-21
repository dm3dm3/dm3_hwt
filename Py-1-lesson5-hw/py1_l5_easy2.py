# coding : utf-8
# PEP-8
# Python-1-lesson5-easy Task 2

import sys
import os


def dirs_in  (current_dir):
    """Ф-ия выводит поддиректории указанной директории"""
    print('директория {} содержит следующие подпапки:'.format(current_dir))
    count_dirs = 0
    for dir_in in os.listdir(current_dir):
        if os.path.isdir(dir_in):
            print('\t--', dir_in)
            count_dirs += 1
    if count_dirs == 0:
        print('\tПодпапок нет.')


dirs_in(os.getcwd())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
