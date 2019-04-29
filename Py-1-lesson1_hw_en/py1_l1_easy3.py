# coding : utf-8
# PEP-8
# Python-1-lesson1-easy Task 3
import time

vuser = input ('Enter your age: \n')
if 3 >= len(vuser) > 0 and vuser.isdigit():
    if int(vuser) <= 17:
        print ('Sorry, using this resource is only 18 years old')
    elif int(vuser) >= 95:
        print('Dear, this content at your age is dangerous to health!')
    else:
        print('Access is allowed. Content 18+: \n\t Pls wait ')
        ind = 0
        while ind < 15:
            time.sleep (0.25)
            print('.')
            ind +=1
else:
    print('It\'s not your age. Sorry, bro!')