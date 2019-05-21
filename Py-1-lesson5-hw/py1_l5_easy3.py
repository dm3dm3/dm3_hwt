# coding : utf-8
# PEP-8
# Python-1-lesson5-easy Task 3

import sys
import os
import shutil


def copy_file(in_file, out_file):
    """Ф-ия выводит поддиректории указанной директории"""
    print('Копирую файл {}.\n Файл {} будет заменён, если уже существует.'.format(in_file, out_file))
    try:
        out_file = shutil.copyfile(in_file, out_file)
        print('копирование в {} прошло успешно'.format(out_file))
    except shutil.SameFileError:
        print('Вы пытались скопировать файл сам в себя!')


input_file = os.path.abspath(sys.argv[0])
# работает и с input_file = sys.argv[0] - но предпочтительно считаю указать полный путь
part_path, type_file = os.path.splitext(input_file)
output_file = part_path + '_copy' + type_file
copy_file(input_file, output_file)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
