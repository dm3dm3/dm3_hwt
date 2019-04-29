# coding : utf-8
# PEP-8
# Python-1-lesson1-easy Task 2

vuser = input ('Enter digit: \n')
if len(vuser) > 0 and vuser.isdigit():
    print('Result your digit + 2 = ', int(vuser) + 2)
else:
    print('It\'s not digit. Sorry, bro!')
