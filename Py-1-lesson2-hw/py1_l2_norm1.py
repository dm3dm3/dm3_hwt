# coding : utf-8
# PEP-8
# Python-1-lesson2-normal Task 1


listnum = [1, -2, 3, 4, -25, 15, 100 , 121, -1, 7, 44, 8, 36]
listres = []
listgarb = []
listcom = []

for ind in listnum:
    if ind < 0:
        #print(f'can\'t do it for {ind}')
        rcom = [f'-i*{abs(ind)**(1/2)}',f'i*{abs(ind)**(1/2)}']
        listcom += rcom
    elif (ind**(1/2) % 1) == False:
        # print(f'int - {ind**(1/2)}')
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

