class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.n = name
        self.c = color
        self.s = speed
        self.police = is_police

    def go(self):
        print(f'{self.n} поехала')

    def stop(self):
        print(f'{self.n} остановилась')

    def turn(self, direction):
        self.d = direction
        print(f'{self.n} повернула {self.d}')

    def show_speed(self):
        print(f'{self.n} едет со скоростью {self.s}')


class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            print(f'{self.c} {self.n} превысил разрещенную скорость на {self.s - 60} км/ч')
        else:
            Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            print(f'{self.c} {self.n} превысил разрещенную скорость на {self.s - 40} км/ч')
        else:
            Car.show_speed(self)


class SportCar(Car):

    def go(self):
        print(f'поехал спорт кар')


class PoliceCar(Car):

    def go(self):
        print(f'Полицейская {self.n} выехала')


tc = TownCar(60, 'желтая', 'LADA 4X4')
tc.go()
tc.show_speed()
tc.turn('направо')
tc.stop()

wc = WorkCar(55, 'синий', 'МТЗ-64')
wc.show_speed()
wc.stop()

pc = PoliceCar(90, 'белая', 'BMW', True)
pc.go()
pc.show_speed()
