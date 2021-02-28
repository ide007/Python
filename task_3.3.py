my_list = ["Иван", "Мария", "Ольга", "Петр", "Илья", "Игорь", "Оксана"]
my_dict = {}


def thesaurus(*args):
    for idx, val in enumerate(*args):
        if val[0] in my_dict.keys():
            my_dict[val[0]].append(val)
        else:
            my_dict.setdefault(val[0], [val])


thesaurus(my_list)
sort_dict = list(my_dict.keys())# не понял как делать распаковку.
sort_dict.sort()
for i in sort_dict:
    print(i, ':', my_dict[i], end=' ')
#print(my_dict) # по принту выдает только ключи.
