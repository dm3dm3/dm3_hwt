# coding : utf-8
# PEP-8
# Python-1-lesson1-normal Task 1
vuint = 0

while 0 >= vuint or vuint >= 10:
    vuser = input('Enter digit from 0 to 10 (exclude): \n')
    if len(vuser) > 0 and vuser.isdigit():
        print('Try again, bro! \n')
        vuint = int(vuser)
        continue
    else:
        print('Your input incorrect. Sorry, bro!\n')
        continue
print ('\t Summare ', vuint, '^2: ', vuint ** 2)

