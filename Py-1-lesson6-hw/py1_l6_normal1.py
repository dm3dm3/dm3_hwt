# coding : utf-8
# PEP-8
# Python-1-lesson6-normal Task 1

import random
import time
#######################################################################################


class Person:
    """
    Персона
    """
    def __init__(self, name, damage = 10, armor = 10):
        self.health = 100
        self.name = name
        self.damage = damage
        self.armor = armor
        self.fighter_title()

    def calc_my_damage(self, damage_enemy): # не совсем понимаю зачем инкапсудировать этот метод
        """подсчёт урона"""
        return damage_enemy // 3 - self.armor // (10/self.coeficient())

    def _create_attack(self): # подготовка аттаки - вот, что надо скрыть
        """подготовка аттаки"""
        return ((self.damage - (self.armor // 15)) * self.coeficient()) // 1

    def  coeficient(self):
        """Коэфициент измотанности"""
        return (self.health + 50) / 150


    def fighter_title(self):
        """вывеска бойца"""
        class_name = str(self.__class__).split('.')[1].split('\'')[0]
        print(f'На ринг выходит боец: {self.name} из команды: {class_name} с навыками атаки: {self.damage} ед. '
              f'и защиты: {self.armor} ед.')

    def get_attack_power(self):
        """проведение атаки"""
        print(f'Боец {self.name} наносит свой удар мощностью  {self._create_attack()} ед.')
        return self._create_attack()
########################################################################################################


class Player(Person):
    """
    Класс игроков
    """
    pass


class Enemy(Person):
    """
    Класс противников
    """
    pass
###########################################################################################################


class FightProcess:
    """
    Класс боя
    """
    def __init__(self, banner = 'Mortal Kombat XX'):
        self.banner = banner
        self.player, self.enemy = self.start_show()
        self.player1, self.player2 = self.fight_random()

    def create_proper(self):
        """Боевые навыки бойцов"""
        while True:
            damage = random.randint(15,100)
            armor = random.randint (15,100)
            if  120 < damage+armor < 160 and damage >= armor:
                return damage, armor

    def start_show(self):
        """Начало боя - представление и создание бойцов"""
        print(f'Ннннннннн-начинается бой {self.banner}, представляем бойцов!')
        player_name = input('Введите имя вашего героя: ')
        player_damage, player_armor = self.create_proper()
        enemy_name = input('Введите имя вашего противника: ')
        enemy_damage, enemy_armor = self.create_proper()
        print('В левом углу ринга наш великолепный герой:')
        player = Player(player_name, player_damage, player_armor)
        print('В левом углу ринга наш несокрушимый до сих пор:')
        enemy = Enemy(enemy_name, enemy_damage, enemy_armor)
        input('Вы готовы? к бою?')
        return player, enemy

    def fight_random(self):
        """Колесо фортуны - выбор 1го атакуещего"""
        if random.randint(0,1) == 1:
            player1 = self.player
            player2 = self.enemy
        else:
            player2 = self.player
            player1 = self.enemy
        return player1, player2

    def fight_round1(self):
        """Ответный удар - 1ого игрока"""
        attack_power = self.player1.get_attack_power()
        losses = self.player2.calc_my_damage(attack_power)
        self.player2.health = self.player2.health - losses
        print(f'{self.player2.name} получает урона на {losses} ед. и его самочувствие оценивается как {self.player2.health} ед.')
        time.sleep(1)

    # Можно сделать одной ф-ией - но пока не хватает на украшательство времени

    def fight_round2(self):
        """Ответный удар - 2ого игрока"""
        print('Ответный удар')
        attack_power = self.player2.get_attack_power()
        losses = self.player1.calc_my_damage(attack_power)
        self.player1.health = self.player1.health - losses
        print(f'{self.player1.name} получает урона на {losses} ед. и его самочувствие оценивается как {self.player1.health} ед.')

    def fight(self):
        """Бой"""
        round = 1
        while True:
            input('\nРаунд: {} \t Начали?'.format(round))
            # в идеале можно сделать отдельную ф-ию на оступившихся - при наличии времени
            if self.player1.health % 11 == 0:
                print(f'Боец {self.player1.name} оступился и не смог нанести удар.')
            else:
                self.fight_round1()
            if self.player2.health % 11 == 0:
                print(f'Боец {self.player2.name} оступился и не смог нанести удар.')
            else:
                self.fight_round2()
            if self.player1.health <= 0 and self.player2.health <= 0:
                print('\n\tНичья! Оба бойца бились до последнего!')
                return
            elif self.player1.health <= 0 and self.player2.health > 0:
                print(f'\n\tБоец {self.player2.name} победил. Боец {self.player1.name} погиб в бою.')
                return
            elif self.player2.health <= 0 and self.player1.health > 0:
                print(f'\n\tБоец {self.player1.name} победил. Боец {self.player2.name} погиб в бою.')
                return
            else:
                round +=1

"""честно говоря - в моей концепции можно было обойтись одним типом бойцов - т.к. по сути разницы в игроке и противнике нет: по заданию создал наследование и ещё 
2 класса - это усложнило немного реализацию: я так прочитал задачу"""
########################################################################################################

fight1 = FightProcess()
fight1.fight()
print('***' * 10)

fight2 = FightProcess('Уличное месилово')
fight2.fight()

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с
# учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю
# на ваше усмотрение.
