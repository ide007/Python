class OwnError(Exception):
    def __init__(self, text):
        self.txt = text


class CheckType:
    def __init__(self):
        self.num_list = []

    def check_value(self):
        global num
        while True:
            try:
                try:
                    num = int(input('Введите число: '))
                    question = input(f'"{num}" в списке. Для продолжения нажмите "Enter". Выход: "q"').lower()
                    self.num_list.append(num)
                    if question == 'q':
                        print('Получился список: ', self.num_list)
                        break
                except ValueError:
                    raise OwnError('Некоректное значение!')
            except (OwnError, ValueError):
                question = input(f'Вы ввели не число! Для продолжения нажмите "Enter". Выход: "q"').lower()
                if question == 'q':
                    print('Получился:', self.num_list)
                    break


item = CheckType()
item.check_value()
