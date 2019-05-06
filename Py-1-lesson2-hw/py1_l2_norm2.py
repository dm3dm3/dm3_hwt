# coding : utf-8
# PEP-8
# Python-1-lesson2-normal Task 2
import time
import datetime


inpdate = input('Enter DATE in DD.MM.YYYY format:')
inday, inmonth, inyear = inpdate.split('.')

while 1 > int(inday) or int(inday) > 31 or 1 > int(inmonth) or int(inmonth) > 12 \
        or len(inyear) != 4 or len(inday) != 2 or len(inmonth) != 2:
    print('Incorrect input. \t Please repeate!')
    inpdate = input('Enter DATE in DD.MM.YYYY format:')
    inday, inmonth, inyear = inpdate.split('.')


# Решение с помощью подключения модулей time and datetime.
print('\n\t Solve of task by modules: time and datetime')
inpform_date=time.strptime(inpdate, '%d.%m.%Y')
inp_timestamp = time.mktime(inpform_date)
print('In text format: {} year.'.format(time.ctime(inp_timestamp)))

# Решение с использованием биллиотик (рукописных).
print('\n\t Trivial solve of task: time and datetime')
date_lib = {'decdate': [' ', ' ', 'двадцать', 'тридцать'],
            'month': ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'],
            'uni': ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
                    'одиннадцатое', 'двенадцатое', 'тридцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое',
                    'дводцатое', 'тридцатое']}

iinday, iinmonth = int(inday), int(inmonth)
dec_in=iinday // 10
if dec_in == 1 or iinday == 20:
    uni = iinday - 1
    dec_in = 1
elif iinday == 30:
    uni = 20
    dec_in = 1
else:
    uni = iinday % 10 - 1
outpdate_str = date_lib['decdate'][dec_in] + ' ' + date_lib['uni'][uni] + ' ' + date_lib['month'] [iinmonth-1]

print(f'Вы хотите сказать: {outpdate_str} {inyear} года?')

##############################################################################
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
