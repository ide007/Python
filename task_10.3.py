class Cell:

    def __init__(self, c):
        self.cells = int(c)

    def __add__(self, other):
        return f'Результат сложения двух клеток: {self.cells + int(other.cells)} ячеек(и).'

    def __sub__(self, other):
        rez = self.cells - other.cells
        return f'Клетка уменьшилась, и равна: {rez} ячейкам' if rez > 0 else 'Так дело не пойдёт :('

    def __mul__(self, other):
        return f'Результат умножения двух клеток: {self.cells * int(other.cells)} ячеек(и).'

    def __truediv__(self, other):
        return f'Результат деления двух клеток: {self.cells // int(other.cells)} ячеек(и).'

    def make_order(self, l):
        rezu = ''
        for i in range(int(self.cells / l)):
            rezu += '*' * l + '\n'
        rezu += '*' * (self.cells % l) + '\n'
        return rezu


c_1 = Cell(43)
c_2 = Cell(9)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(10))
