# coding : utf-8
# PEP-8
# Python-1-lesson2-easy Task 1

fruits = ['яблоко', 'банан', 'киви', 'арбуз']
for ind in fruits:
    # print(ind)
    # print(fruits.index(ind))
    print('Fruit num. {1} - it\'s: {0}'.format(ind, fruits.index(ind) ) )
# с помощью метода и цикла

print('\t OR')

for ind in range(len(fruits)):
    print('Fruit num. {} - it\'s: {}'.format(ind, fruits[ind] ) )
#с помощью ф-ии определения длины

