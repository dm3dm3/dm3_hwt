# coding : utf-8
# PEP-8
# Python-1-lesson2-normal Task 4

list1 = [1,2,3,4,5,6,7,8,8,7,6,'salt',4,2,0,8,9,2,'salt']
set1 = set(list1)
lista = list(set1)
print('\tInput:\n\t', list1)
for elem in lista:
    if list1.count(elem) > 1:
        for _ in range(list1.count(elem)):
            list1.remove(elem)
    else:
        continue
listb = list1
print('Output of point A:\n\t', lista)
print('Output of point B:\n\t', listb)
print('Ordered list B:\n\t', set(listb))

###############################################################################

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
