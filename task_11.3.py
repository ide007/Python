class OwnError(Exception):
    def __init__(self, text):
        self.txt = text


num_list = []
while True:
    try:
        try:
            num = int(input('\rВведите число: '))
            question = input(f'"{num}" в списке. Для продолжения нажмите "Enter". Выход: "q"').lower()
            num_list.append(num)
            if question == 'q':
                print('Получился список: ', num_list)
                break
        except ValueError:
            raise OwnError('Некоректное значение!')
    except (OwnError, ValueError):
        question = input(f'Вы ввели не число! Для продолжения нажмите "Enter". Выход: "q"').lower()
        if question == 'q':
            print('Получился:', num_list)
            break
