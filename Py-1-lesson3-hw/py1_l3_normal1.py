# coding : utf-8
# PEP-8
# Python-1-lesson3-normal Task 1

import random
import time

# Функция делает из 2х входных списков  - словарь.
# И по словарю создаёт зарплатную ведомость известного формата
# На выходе позиция начала самой ведомости

def print_cash_list(filename, name_list, cash_list):

    l_namel = len(max(max(name_list, key=len), 'Имя:', key=len))
    l_cashl = len(max(str(max(cash_list)), 'Зарплата:', key=len))
    cash_dict = dict(zip(name_list, cash_list))

    print('Запишем в: ', filename)
    cash_file = open(filename, 'w', encoding='UTF-8')
    cash_file.write('\t\t ЗАРПЛАТЫ СОТРУДНИКАМ НА ДАТУ:\n\t\t {} {} {} года '.format(date, month, year))
    cash_file.write('\n\n' + 'Имя:'.rjust(l_namel, ' ') + ' - ' + 'Зарплата:'.ljust(l_cashl, ' ') + '  руб.' + '\n\n')
    cash_file.close()

    with open(filename, 'a', encoding='UTF-8') as cash_file:
        pos_body_start = cash_file.tell()
        for hum_name, money in cash_dict.items():
            cash_file.write(hum_name.rjust(l_namel, ' ') + ' - ' + str(money).ljust(l_cashl, ' ') + '\n')
    return (pos_body_start)

# Функция выводит информацию из зарплатной ведомости с вычетом налогов и укрываением сверхдоходных лиц
# На выходе ф-ии None

def output_cash_list(filename, pos_read):
    cash_limit = int(input('\n\tВведите "потолок" зарплаты в руб. без коп.: '))
    print('\nПрочитаем данные из: {} \n\n\t Зарплаты сотрудников представленны за вычетом налогa (13%)'
          ' в руб.:'.format(filename))
    with open(filename, 'r', encoding='UTF-8') as cash_file:
        cash_file.seek(pos_read, 0)
        for line in cash_file:
            hum_name, money = line.split(' - ')
            if int(money) >= cash_limit:
                continue
            else:
                roubl, copp = str(round(int(money) * 0.87, 2)).split('.')
                print(f'{hum_name.upper()} получает после уплаты налогов {roubl} руб. {copp} коп.')

#тело программы: генерятся списки, имя зарплатной ведомости и дёргаются ф-ии

name_list = ['Зашеида','Мейлиль','Ндарис','Хиранель','Эрин','Финелджа','Торбера','Реберн','Гортрисс','Дрит','Вил','Баша','Думеин','Мэлиамнэ',
             'Амастасия','Дмитрий','Семён','Ольга','Урбек','Иван','Асхан','Зина','Николай','Валентин','Светлана','Евгения']
cash_list = list()
for _ in range(len(name_list)):
    cash_list.append(random.randint(25000, 580000))

day, month, date, time, year = str(time.ctime(time.time())).split(' ',4)
filename = f'cashflow_{date}_{month}_{year}.txt'

pos_read = print_cash_list(filename, name_list=name_list, cash_list=cash_list)
output_cash_list(filename,pos_read)

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
