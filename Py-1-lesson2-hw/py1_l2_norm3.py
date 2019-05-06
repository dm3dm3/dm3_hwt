# coding : utf-8
# PEP-8
# Python-1-lesson2-normal Task 3
import time
import datetime
import random

rlist = []
inpn = input('Enter count of elements in list:')
inpint=int(inpn)
for _ in range(inpint):
    rlist.append(random.randint(-100, 100))
print(f'Output of randomize:\n\t {rlist}')

##################################################################################
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
