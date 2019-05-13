# coding : utf-8
# PEP-8
# Python-1-lesson2-easy Task 3


listint = [1,2,3,4,5, 15,  20 ,33, 1,7, 14]
listres = []

for ind in listint:
    if (ind % 2):
        listres.append(ind*2)
    else:
        listres.append(ind / 4)
print('\t LIST input')
print(listint)
print('\t LIST output')
print(listres)

######################################################################################
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
