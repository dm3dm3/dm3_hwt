# coding : utf-8
# PEP-8
# Python-1-lesson1-normal Task 2
import time

vusera = input ('Enter your A: ')
vuserb = input ('\nEnter your B: ')

if len(vusera) > 0 and len(vuserb) > 0:
    print('\n\tBefore focus: Youre A:', vusera, 'Youre B:', vuserb)
    vusera, vuserb = vuserb, vusera
    print ('Press Enter!')
    ent = input ('Tr... ' * 3)
    time.sleep(0.5)
    print('\n\tAfter focus: Youre A:', vusera, 'Youre B:', vuserb, '\n', '\tVualya' * 2)
else:
    print('Your input incorrect. Sorry, bro!\n')