# coding : utf-8
# PEP-8
# Python-1-lesson2-easy Task 2


list1 = [1,2,3,4,'word',[0,1,0,1],0,9, ['i','m'], 2, 'word', 'word3', 2]
list2 = [2,4,'word2',[0,0,0,0],['i','m'], 'word']
print('\t LIST - 1')
print(list1)
print('\t LIST - 2')
print(list2)
print('\t RESULT = LIST-1 and LIST-2 diffents')

delel = []
for ind in list2:
    while ind in list1:
        #
        # Another way
        # list1.remove(ind)
        #
        el = list1.index(ind)
        delel.append(list1.pop(el))

print(list1)
print(f'\nThere were deleted the following elements:{delel}')

################################################################
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
