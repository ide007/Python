class Stationery:

    def __init__(self, title):
        self.t = title

    def draw(self):
        print(f'{self.t} - Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Starting rendering - {self.t}')


class Pencil(Stationery):
    def draw(self):
        print(f'Rendering starting- {self.t}')


class Handle(Stationery):
    def draw(self):
        print(f'Select with - {self.t}')


item_1 = Pen('pen')
item_1.draw()
item_2 = Pencil('pencil')
item_2.draw()
item_3 = Handle('handle')
item_3.draw()
