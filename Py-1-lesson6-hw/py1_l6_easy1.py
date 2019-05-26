# coding : utf-8
# PEP-8
# Python-1-lesson6-easy Task 1
#######################################################################################


class TownCar:
    """
    Класс для городской машины
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self._direct = 0
        self._is_police = False
        self.show_room()

    def go (self, speed_up):
        step = (int(speed_up) - self.speed) / 10
        for _ in range(10):
            self.speed = self.speed + step
            print('Cкорость: {} км/ч'.format(self.speed))
        print('Автомобиль двигается со скростью {} км/ч'.format(self.speed))


    def stop (self):
        if self.speed <= 0:
            self.speed = 0
        else:
            step = self.speed / 4
            for _ in range(4):
                self.speed = self.speed - step
                print('Погосили скорость:', self.speed)
        print('Автомобиль полностью остановлен!')


    def turn (self, direction):
        self._direct = (self._direct + direction + 3600) % 360
        if 5 <= self._direct < 45:
            print(f'Ваш автомобиль направлен правее, под углом {self._direct} градусов от направления "к цели"')
        elif 45 <= self._direct <= 135:
            print(f'Ваш автомобиль направлен вправо, под углом {self._direct} градусов от направления "к цели"')
        elif 135 < self._direct <= 175:
            print(f'Ваш автомобиль направлен правее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 175 < self._direct < 185:
            print(f'Ваш автомобиль направлен обратно, под углом {self._direct} градусов от направления "к цели"')
        elif 185 <= self._direct < 225:
            print(f'Ваш автомобиль направлен левее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 225 <= self._direct <= 315:
            print(f'Ваш автомобиль направлен влево, под углом {self._direct} градусов от направления "к цели"')
        elif 315 < self._direct <= 355:
            print(f'Ваш автомобиль направлен левее, под углом {self._direct} градусов от направления "к цели"')
        else:
            print(f'Ваш автомобиль направлен прямо, под углом {self._direct} градусов от направления "к цели"')


    def show_room(self):
        class_name = str(self.__class__).split('.')[1].split('\'')[0]
        print(f'Автомобиль {self.name}, {self.color} цвета, классивицируется как: {class_name}')


    def get_isitcops(self):
        print('Легавые!!!' if self._is_police else 'Продолжаем расслабляться...')
########################################################################################################


class WorkCar:
    """
    Класс для Рабочих машин
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self._direct = 0
        self._is_police = False
        self.show_room()


    def go (self, speed_up):
        step = (int(speed_up) - self.speed) / 10
        for _ in range(10):
            self.speed = self.speed + step
            print('Cкорость: {} км/ч'.format(self.speed))
        print('Автомобиль двигается со скростью {} км/ч'.format(self.speed))


    def stop (self):
        if self.speed <= 0:
            self.speed = 0
        else:
            step = self.speed / 5
            for _ in range(5):
                self.speed = self.speed - step
                print('Погосили скорость:', self.speed)
        print('Автомобиль полностью остановлен!')


    def turn (self, direction):
        self._direct = (self._direct + direction + 3600) % 360
        if 5 <= self._direct < 45:
            print(f'Ваш автомобиль направлен правее, под углом {self._direct} градусов от направления "к цели"')
        elif 45 <= self._direct <= 135:
            print(f'Ваш автомобиль направлен вправо, под углом {self._direct} градусов от направления "к цели"')
        elif 135 < self._direct <= 175:
            print(f'Ваш автомобиль направлен правее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 175 < self._direct < 185:
            print(f'Ваш автомобиль направлен обратно, под углом {self._direct} градусов от направления "к цели"')
        elif 185 <= self._direct < 225:
            print(f'Ваш автомобиль направлен левее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 225 <= self._direct <= 315:
            print(f'Ваш автомобиль направлен влево, под углом {self._direct} градусов от направления "к цели"')
        elif 315 < self._direct <= 355:
            print(f'Ваш автомобиль направлен левее, под углом {self._direct} градусов от направления "к цели"')
        else:
            print(f'Ваш автомобиль направлен прямо, под углом {self._direct} градусов от направления "к цели"')


    def show_room(self):
        class_name = str(self.__class__).split('.')[1].split('\'')[0]
        print(f'Автомобиль {self.name}, {self.color} цвета, классивицируется как: {class_name}')


    def get_isitcops(self):
        print('Легавые!!!' if self._is_police else 'Продолжаем расслабляться...')
####################################################################################


class SportCar:
    """
    Класс для спортивных машин
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self._direct = 0
        self._is_police = False
        self.show_room()


    def go (self, speed_up):
        step = (int(speed_up) - self.speed) / 5
        for _ in range(5):
            self.speed = self.speed + step
            print('Cкорость: {} км/ч'.format(self.speed))
        print('Автомобиль двигается со скростью {} км/ч'.format(self.speed))


    def stop (self):
        if self.speed <= 0:
            self.speed = 0
        else:
            step = self.speed / 4
            for _ in range(4):
                self.speed = self.speed - step
                print('Погосили скорость:', self.speed)
        print('Автомобиль полностью остановлен!')


    def turn (self, direction):
        self._direct = (self._direct + direction + 3600) % 360
        if 5 <= self._direct < 45:
            print(f'Ваш автомобиль направлен правее, под углом {self._direct} градусов от направления "к цели"')
        elif 45 <= self._direct <= 135:
            print(f'Ваш автомобиль направлен вправо, под углом {self._direct} градусов от направления "к цели"')
        elif 135 < self._direct <= 175:
            print(f'Ваш автомобиль направлен правее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 175 < self._direct < 185:
            print(f'Ваш автомобиль направлен обратно, под углом {self._direct} градусов от направления "к цели"')
        elif 185 <= self._direct < 225:
            print(f'Ваш автомобиль направлен левее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 225 <= self._direct <= 315:
            print(f'Ваш автомобиль направлен влево, под углом {self._direct} градусов от направления "к цели"')
        elif 315 < self._direct <= 355:
            print(f'Ваш автомобиль направлен левее, под углом {self._direct} градусов от направления "к цели"')
        else:
            print(f'Ваш автомобиль направлен прямо, под углом {self._direct} градусов от направления "к цели"')


    def show_room(self):
        class_name = str(self.__class__).split('.')[1].split('\'')[0]
        print(f'Автомобиль {self.name}, {self.color} цвета, классивицируется как: {class_name}')


    def get_isitcops(self):
        print('Легавые!!!' if self._is_police else 'Продолжаем расслабляться...')
####################################################################################


class PoliceCar:
    """
    Класс для полицейских машин
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self._direct = 90
        self._is_police = True
        self.show_room()


    def go (self, speed_up):
        step = (int(speed_up) - self.speed) / 10
        for _ in range(10):
            self.speed = self.speed + step
            print('Cкорость: {} км/ч'.format(self.speed))
        print('Автомобиль двигается со скростью {} км/ч'.format(self.speed))


    def stop (self):
        if self.speed <= 0:
            self.speed = 0
        else:
            step = self.speed / 4
            for _ in range(4):
                self.speed = self.speed - step
                print('Погосили скорость:', self.speed)
        print('Автомобиль полностью остановлен!')


    def turn (self, direction):
        self._direct = (self._direct + direction + 3600) % 360
        if 5 <= self._direct < 45:
            print(f'Ваш автомобиль направлен правее, под углом {self._direct} градусов от направления "к цели"')
        elif 45 <= self._direct <= 135:
            print(f'Ваш автомобиль направлен вправо, под углом {self._direct} градусов от направления "к цели"')
        elif 135 < self._direct <= 175:
            print(f'Ваш автомобиль направлен правее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 175 < self._direct < 185:
            print(f'Ваш автомобиль направлен обратно, под углом {self._direct} градусов от направления "к цели"')
        elif 185 <= self._direct < 225:
            print(f'Ваш автомобиль направлен левее и назад, под углом {self._direct} градусов от направления "к цели"')
        elif 225 <= self._direct <= 315:
            print(f'Ваш автомобиль направлен влево, под углом {self._direct} градусов от направления "к цели"')
        elif 315 < self._direct <= 355:
            print(f'Ваш автомобиль направлен левее, под углом {self._direct} градусов от направления "к цели"')
        else:
            print(f'Ваш автомобиль направлен прямо, под углом {self._direct} градусов от направления "к цели"')


    def show_room(self):
        class_name = str(self.__class__).split('.')[1].split('\'')[0]
        print(f'Автомобиль {self.name}, {self.color} цвета, классивицируется как: {class_name}')


    def get_isitcops(self):
        print('Легавые!!!' if self._is_police else 'Продолжаем расслабляться...')
####################################################################################

car1 = TownCar('Nissan', 'black')
car1.stop()
car1.get_isitcops()
print('-*-'*20)
car2 = WorkCar('Toyota', 'white')
car2.turn(-50)
print('-++-'*20)
car3 = SportCar('Ferrari', 'red')
car3.go(120)
car3.stop()
print('/-\\'*20)
car4 = PoliceCar('Ford', 'blue')
car4.turn(408)
car4.get_isitcops()
print('++\\'*20)

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
