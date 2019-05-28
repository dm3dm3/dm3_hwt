# coding : utf-8
# PEP-8
# Python-1-lesson7-LOTO

import random
import time
import sys


class LotoCard:
    # Создаём карточки игроков: параметры для расширения игрового процесса - в т.ч. для мультиплея
    def __init__(self, count_cards=2, rows=3, len_row=5):
        self.rows = rows
        self.count_cards = count_cards
        self.len_row = len_row
        self.get_cards()

    def _new_card(self):
        #создание новой карточки
        setnums = set()
        while len(setnums) < self.rows * self.len_row:
            setnums.add(random.randint(1, 90)) #список, чтобы не было повторов в карточке
        listnums = list(setnums)
        random.shuffle(listnums) # перемешаем числа
        card = [listnums[i: i + self.len_row] for i in range(0, len(listnums), self.len_row)]
        for i in range(len(card)):
             card[i].sort()
        return card[:]

    def get_cards(self):
        # создание карточек игроков - надо будет вытаскивать наружу для масштабирования
        self.card_user = self._new_card()
        self.card_comp = self._new_card()

class LotoPlayer(LotoCard):
    # создание игроков и карточки для игроков
    def __init__(self, name='Player'):
        super().__init__()
        self.name = name
        self.hit = 0
        self.tabs = self.tabulation_g(self.len_row, self.rows)

    @staticmethod
    def tabulation_g(rowlen, rows):
        #генерация - надо бы переделать на next - чтобы не привязываться
        tabs=[[],[],[]] #порнография - надо подумать как поправить
        for istr in range(rows):
            tab = list(random.randint(0,5) for _ in range(rowlen))
            tabs[istr] = tab
        return tabs

    def show_card(self, play_card):
        #отображение  карточки
        tabz=self.tabs
        print('{:-^26}'.format(self.name))
        for istr in range(self.rows):
            print('{0[0]:>{1[0]}} {0[1]:>{1[1]}} {0[2]:>{1[2]}} {0[3]:>{1[3]}} {0[4]:>{1[4]}}'.
                  format(play_card[istr],tabz[istr]))
        print('-'*26)


    def search(self, play_card, num_keg):
        # Поиск номера на карточке и определение выйгравшего
        for ind_num, user_num in enumerate(play_card):
            if num_keg in user_num:
                play_card[ind_num][user_num.index(num_keg)] = 'X'
                self.hit += 1
                if self.hit == 15:
                    print('\n\t{} Победил!'.format(self.name))
                    sys.exit(1)
                return True
        return False


class LotoBag:
    # Достаем бочонки из мешка
    def __init__(self, count):
        self.count = count
        self.newkeg = self.generator()

    def generator(self):
        # Сформируем последовательность в виде листа и хорошенько перемешаем (тем самым исключим повторы)
        # всё как в мешочке с бочонками
        glist = [x for x in range(1, self.count + 1)]
        random.shuffle(glist)
        for ind_keg, num_keg in enumerate(glist):
            print('=' * 40)
            print('Новый бочонок: {} (осталось {})'.format(num_keg, self.count - (ind_keg + 1)))
            yield num_keg # перебираем в генераторе через for и передаём значение в next


def play_loto_game(enemy):
    # сам игровой прроцесс
    card = LotoCard()
    bag = LotoBag(90)

    player1 = LotoPlayer(input_name())
    player1.show_card(card.card_user)
    player2 = LotoPlayer(enemy)
    print(f'\nПриветствуем {enemy} на игре Лото!')
    player2.show_card(card.card_comp)

    input('Для продолжения нажмите "Enter"... ')
    print('\n---=======ИГРА=НАЧАЛАСЬ=======---')

    while True:
        keg_num = next(bag.newkeg)
        player1.show_card(card.card_user)
        player2.show_card(card.card_comp)

        user_input = input('\tЗачеркнуть цифру? (y/n)')
        while user_input != 'n' and user_input != 'y':
            print('Введите "y" или "n"')
            time.sleep(1)
            user_input = input('\tЗачеркнуть цифру? (y/n)')
            continue
        if user_input == 'y':
            if player1.search(card.card_user, keg_num):
                player2.search(card.card_comp, keg_num)
                continue
            else:
                print('\n\tИгра окончина - вы проиграли.')
                sys.exit(1)

        if user_input == 'n':
            if player1.search(card.card_user, keg_num):
                print('\n\tИгра окончина - вы проиграли.')
                sys.exit(1)
            elif player2.search(card.card_comp, keg_num):
                continue



def input_name():
    #Имя игрока - ввод
    name = ''
    while len(name) < 2 or name.isalnum() is not True:
        name = input('Игрок введите ваше имя: ')
    print(f'\nПриветствуем {name.title()} на игре Лото!')
    return name.title()


def lotto_description():
    # правила игры и опрос желания
    print(
    """
    == Лото ==
    
    Правила игры в лото.
    
    Игра ведется с помощью специальных карточек, на которых отмечены числа,
    и фишек (бочонков) с цифрами.
    
    Количество бочонков — 90 штук (с цифрами от 1 до 90).
    
    Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
    расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
    
    --------------------------
        9 43 62          74 90
     2    27    75 78    82
       41 56 63     76      86
    --------------------------
    
    В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
    случайная карточка.
    
    Каждый ход выбирается один случайный бочонок и выводится на экран.
    Также выводятся карточка игрока и карточка компьютера.
    
    Игроку предлагается зачеркнуть соотв. бочёнку поле на карточке после чего продолжить
     или продолжить сразу, если такое поле отсутствует в карточке игрока.
    
    Побеждает тот, кто первый закроет все числа на своей карточке.
    """
    )

    while True:
        user_sel = input('\tВы хотите сыграть в игру ЛОТО? (y/n)')
        if user_sel == 'y':
            print('\n{:.^50}'.format('СТАРТ игры ЛОТО'))
            play_loto_game('Компьютер')
            print('\n{:-^50}\n'.format('Игра закончена'))
        elif user_sel == 'n':
            break


# запуск игры
if __name__ == '__main__':
    play_loto_game('= P C =')
else: lotto_description()


# """
# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
#
# """
