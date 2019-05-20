# coding : utf-8
# PEP-8
# Python-1-lesson4-easy Task 1

import random
import copy


def randlist_num (count, start, stop):
    """ Функция создаёт список из чисел """
    list_out=[random.randint(start,stop) for _ in range(count)]
    return list_out


list_input = copy.deepcopy(randlist_num(20, start=-20, stop=20)) #в данном случае не обязательно, но в случае многократного использования ф-ии - лучше так
list_output = [sqnum ** 2 for sqnum in list_input]

print ('Input = ',list_input)
print ('Output: input^2 = ', list_output)


# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
