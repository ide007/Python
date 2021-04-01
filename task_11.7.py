class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'Сумма равна: {self.x + other.x} + {self.y + other.y}*i'

    def __mul__(self, other):
        return f'Произведение равно: {self.x * other.x - self.y * other.y} + {self.y * other.x + self.x * other.y}*i'


z_1 = ComplexNum(7, 3)
z_2 = ComplexNum(6, 2)
print(z_1 + z_2)
print(z_1 * z_2)
