# coding : utf-8
# PEP-8
# Python-1-lesson1-easy Task 1

vera = 10 ** 4
verb = 10.1
verc = False
vuser = input ('Enter youre msg for world: \n')
vlisttyp = (type(vera), type(verb), type(verc), type(vuser))
vlistcount = (vera, verb, verc, vuser)


print(vlisttyp)
print(vlistcount)

tablev = (vlistcount, vlisttyp)

print(tablev)


tablev_2 = list (zip (*tablev))
print(tablev_2)

print('*' * 15)
print('\n\tResult:\n\n\t')
i = 0
for i in tablev_2:
    print(i)
