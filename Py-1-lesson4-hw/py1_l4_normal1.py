# coding : utf-8
# PEP-8
# Python-1-lesson4-normal Task 1

import random
import copy
import re


def user_input (subject):
    """ Функция ввода данных """
    input_str=input(f'\tПользователь, введите пожалуйста {subject}: ')
    while len(input_str) < 2:
        print('\t\tНеверный ввод, повторите!\n')
        input_str=input(f'\tПользователь, введите пожалуйста {subject}: ')
    return input_str


def check_input_correct(pattern_input, subject):
    """Абсолютно-точное соответствие достигается при обозначении конца и начала строки"""
    string = user_input(subject)
    pattern_input = long_user_name_check(pattern_input, string)
    pattern_input = '^' + pattern_input + '$'
    pattern = re.compile(pattern_input)
    while pattern.match(string) is None:
        print('Некорректно введено поле: {}\t- {}, видимо у вас лишниие или некорректные символы: '.format(subject, string))
        string = user_input(subject)
    print(string, "\t - введено верно")
    return string


def long_user_name_check (pattern_input, string):
    """Функция проверки для составных имён"""
    if len(re.findall(pattern_input, string)) > 1:
        print('\tУ вас составное значение в данном поле. Если вы написали его через "-" - всё будет в порядке!')
        parts = len(re.findall(pattern_input, string))
        pattern_input = (pattern_input + '[-]*') * parts
    return  pattern_input


name_user='имя'
surname_user = 'фамилию'
email_user = 'электронную почту'
pattern_name_def = r'([A-Z]{1}|[А-Я]{1})([a-z]+|[а-я])+'
pattern_email_def = r'[a-z0-9]{1}[^\s[A-Z]+@[\w]{1}[^\s[A-Z]+\.[a-z]{2,}'

print (f'\n\tПользователь - {check_input_correct(pattern_name_def, name_user)} {check_input_correct(pattern_name_def, surname_user)}:'
       f' эл.почта - {check_input_correct(pattern_email_def, email_user)}')

# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
