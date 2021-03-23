class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.sn = surname
        self.pos = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.n + ' ' + self.sn

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_1 = Position('Ivan', 'Ivanov', 'Chief', '100000', '100000')
worker_2 = Position('Oleg', 'Petrov', 'Caretaker', '15000', '5000')
print(f'"{Position.get_full_name(worker_1)}" - общий доход: {Position.get_total_income(worker_1)}')
print(f'"{Position.get_full_name(worker_2)}" - общий доход: {Position.get_total_income(worker_2)}')
