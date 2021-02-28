num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
            'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'zero': 'нуль'}


def num_translate_adv(key):
    if key.isalpha():
        if key == key.title():
            key = key.lower()
            if key in num_dict:
                return print(num_dict[key].title())
        elif key in num_dict:
            return print(num_dict[key])
        else:
            print('None')
    else:
        print('Нужно было ввести буквами, например: "one"')


check = input(str('введите прописью числительное от 0 до 10 на английском: '))
num_translate_adv(check)
