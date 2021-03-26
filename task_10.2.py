from abc import ABC, abstractmethod


class Clothe(ABC):
    def __init__(self, val):
        self.value = val

    @abstractmethod
    def calculation(self):
        pass
        # return f'Общий расчёт расхода ткани: {self.value / 6.5 + 0.5 + 2 * self.value + 0.3:.2f}'


class Coat(Clothe):

    def calculation(self):
        return f'Расход ткани на пальто: {self.value / 6.5 + 0.5:.2f}'


class Suit(Clothe):

    def calculation(self):
        return f'Расход ткани на костюм: {self.value * 2 + 0.3:.2f}'

    @property
    def prn(self):
        return Suit.calculation(self)


new_coat = Coat(65)
new_suit = Suit(4)

print(new_coat.calculation())
print(new_suit.prn)     # property
