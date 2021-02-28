def thesaurus_adv(*lis):
    dict_name_surname = {}
    for val in lis:
        nam, sur = val.split()
        surname = dict_name_surname.get(sur[0])
        if surname is None:
            surname = {}
        name = surname.get(nam[0])
        if name is None:
            name = []
        name.append(val)
        surname.setdefault(nam[0], name)
        dict_name_surname.setdefault(sur[0], surname)

    return dict_name_surname


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
