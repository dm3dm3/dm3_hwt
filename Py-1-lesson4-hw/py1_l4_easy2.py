# coding : utf-8
# PEP-8
# Python-1-lesson4-easy Task 2

import random
import copy


def randlist_smth (count, *args):
    """ Функция создаёт случаёный список из входа"""
    list_out=[random.choice(args) for _ in range(count)]
    return list_out


list_input1 = copy.deepcopy(randlist_smth(8, 'яблоко', 'банан', 'киви', 'арбуз', 'груша', 'маракуйа' ,'слива', 'авокадо')) #список1
list_input2 = copy.deepcopy(randlist_smth(8, 'яблоко', 'банан', 'киви', 'арбуз', 'груша', 'маракуйа', 'слива', 'авокадо', 'дыня')) #список2
# можно сделать пользовательский ввод и передавать список и поставить детектор на пустой ввод (IndexError: Cannot choose from an empty sequence)

list_output = set(fruit for fruit in list_input1 if list_input2.count(fruit) is not 0) #set-чтобы убрать повторы #is not можно поменять !=

print ('Vova\'s fruits',list_input1)
print ('Alex\'s fruits', list_input2)
print ('If they get poisoned it may be one of fruits:', list(list_output)) #по условию на выходе должен быть список


# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
