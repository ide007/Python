from random import choice, randrange


def get_jokes(n, repeat=False):
    list_jokes = []
    while n and len(nouns):
        num = randrange(len(adverbs))
        if repeat:
            list_jokes.append(f'{nouns.pop[num]} {adverbs.pop[num]} {adjectives.pop[num]}')
        else:
            list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

        n = n - 1
    return list_jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(int(input("Сколько Вам шуток отвесить?:  "))))
