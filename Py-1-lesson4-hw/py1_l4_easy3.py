# coding : utf-8
# PEP-8
# Python-1-lesson4-easy Task 3

import random
import copy


def randlist_num (count, start, stop):
    """ Функция создаёт список из чисел """
    list_out=[random.randint(start,stop) for _ in range(count)]
    return list_out


list_input = copy.deepcopy(randlist_num(40, start=-50, stop=200)) #входной список
list_output = [filter for filter in list_input if filter > 0 and filter % 3 is 0 and filter % 4 is not 0] #выходной список после проверки 3х условий

print('Input = ',list_input)
print('Output +++ :', list_output)
print('Good values: ', set(list_output))

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
