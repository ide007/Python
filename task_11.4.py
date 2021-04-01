class OfficeEquipment:
    def __init__(self, maker, model, speed, price, quantity=1):
        self.mk = maker
        self.mod = model
        self.sp = speed
        self.pr = price
        self.q = quantity
        self.items = {'Модель устройства': self.mk, 'Количество': self.q, 'Цена': self.pr}

    def income(self):
        try:
            model = self.mod
            price = self.pr
            quantity = self.q
            item = {'Модель устройства': model, 'Цена за ед': price, 'Количество': quantity, 'Общая стоимость': self.q * self.pr}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(OfficeEquipment):
    def __init__(self, maker, model, speed, price, color=False):
        super().__init__(maker, model, speed, price)
        self.mk = maker
        self.mod = model
        self.sp = speed
        self.pr = price
        self.col = color


class CopyMachine(OfficeEquipment):
    def __init__(self, maker, model, speed, price, lan=False):
        super().__init__(maker, model, speed, price)
        self.mk = maker
        self.mod = model
        self.sp = speed
        self.pr = price
        self.lan = lan


class Scan(OfficeEquipment):
    def __init__(self, maker, model, speed, price, resolution):
        super().__init__(maker, model, speed, price)
        self.mk = maker
        self.mod = model
        self.sp = speed
        self.pr = price
        self.dpi = resolution


p_1 = Printer('Oki', 'B431', 25, 950, True)
cop_1 = CopyMachine('Xerox', '3300', 30, 1050)
sc_1 = Scan('Panasonic', 'KV-81', 15, 400, 1200)

p_1.income()
cop_1.income()
sc_1.income()
