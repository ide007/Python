num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
            'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'zero': 'нуль'}


def num_translate(num):
    if num in num_dict:
        print(num_dict[num])
    else:
        print('None')


num_translate(input('введите прописью цифру на английском: '))
