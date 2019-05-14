# coding : utf-8
# PEP-8
# Python-1-lesson3-easy Task 1

def print_data (name, age, city):
    str_return=f'{name}, {age} год(а), проживает в городе {city}'
    return(str_return)
def print_input (name, age, city):
    print(f'\t {name}, {age} год(а)/лет, проживает в городе {city}')


name = input('Введите ваше имя: ')
age = input('Введите ваш возраст: ')
city = input('Введите город проживания: ')
# print восновной программе
print(print_data(name=name, age=age, city=city))
# print вполне можно спрятать в ф-ию
print('\n')
print_input(name, age, city)


# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
