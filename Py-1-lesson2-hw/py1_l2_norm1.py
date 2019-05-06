# coding : utf-8
# PEP-8
# Python-1-lesson2-normal Task 1


listnum = [1, -2, 3, 4, -25, 15, 100 , 121, -1, 7, 44, 8, 36]
listres = []
listgarb = []
listcom = []

for ind in listnum:
    if ind < 0:
        rcom = [f'-i*{abs(ind)**(1/2)}',f'i*{abs(ind)**(1/2)}']
        listcom += rcom
    elif (ind**(1/2) % 1) == False:
        listres.append(int(ind**(1/2)))
    else:
        listgarb.append(ind**(1/2))

print('\t LIST input')
print(listnum)
print('\t LIST output')
print(listres)
print('/\\' * 30)
print('\t LIST complex')
print(listcom)
print('\n\t LIST garbage')
print(listgarb)

###############################################################################
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
