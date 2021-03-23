class Road:

    def __init__(self, long, w):
        self._length = long
        self._width = w
        self.weight = 25
        self.thickness = 5

    def total_weight(self):
        tw = (self._length * self._width * self.weight * self.thickness)/1000
        print(f'Общий вес асфальта необходимово для покрытия дороги {tw} тонн(ы).')


r = Road(5000, 25)
r.total_weight()
