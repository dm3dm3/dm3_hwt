# coding : utf-8
# PEP-8
# Python-1-lesson4-normal Task 2

import random
import copy
import re
#import string

def input_sym_count(pattern_input, string):
    """Функция вычисляет количество появлений искомой операции"""
    count=(len(re.findall(pattern_input, string, re.S)) if re.search(pattern_input, string, re.S) is not None else 0)
    return count


some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

#punkt='[^' + str(string.punctuation).replace('.', '') + ']+'
#Паттерны
pattern_pointbypoint = r'\.'
pattern_pointtextpoint = r'\.[^:;,?!]+'

# будем проверять пока 2 раза подряд обе проверки не станут 0-ми
timer=0
iter=2
while timer < 2:
    count1 = input_sym_count(pattern_pointbypoint * iter, some_str)
    print(f'Последовательность из {iter} точек подряд встречается: {count1} раз в тексте' if count1 > 0
          else f'Последовательность из {iter} точек подряд не встречается в тексте')
    count2 = input_sym_count(pattern_pointtextpoint * iter, some_str)
    print(f'Последовательность из {iter} точек по ходу текста подряд встречается: {count2} раз в тексте\n' if count2 > 0
          else f'Последовательность из {iter} точек по ходу текста подряд не встречается в тексте\n')
    iter += 1
    if (count1 + count2) == 0:
        timer += 1
    else:
        timer = 0

# Эти задачи необходимо решить используя регулярные выражения!

# # Задача - 2:
# # Вам дан текст:
#
# some_str = '''
# Мороз и солнце; день чудесный!
# Еще ты дремлешь, друг прелестный —
# Пора, красавица, проснись:
# Открой сомкнуты негой взоры
# Навстречу северной Авроры,
# Звездою севера явись!
# Вечор, ты помнишь, вьюга злилась,
# На мутном небе мгла носилась;
# Луна, как бледное пятно,
# Сквозь тучи мрачные желтела,
# И ты печальная сидела —
# А нынче... погляди в окно:
# Под голубыми небесами
# Великолепными коврами,
# Блестя на солнце, снег лежит;
# Прозрачный лес один чернеет,
# И ель сквозь иней зеленеет,
# И речка подо льдом блестит.
# Вся комната янтарным блеском
# Озарена. Веселым треском
# Трещит затопленная печь.
# Приятно думать у лежанки.
# Но знаешь: не велеть ли в санки
# Кобылку бурую запречь?
# Скользя по утреннему снегу,
# Друг милый, предадимся бегу
# Нетерпеливого коня
# И навестим поля пустые,
# Леса, недавно столь густые,
# И берег, милый для меня.'''
#
# # Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# # более одной точки, при любом исходе сообщите результат пользователю!
