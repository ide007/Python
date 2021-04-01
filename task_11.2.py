class OwnError(Exception):
    def __init__(self, text):
        self.txt = text


def div():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise OwnError('Делить на нуль нельзя.')
        else:
            return num_1 / num_2
    except ValueError:
        return 'Вы ввели не число'
    except OwnError as err:
        return err


print(div())
