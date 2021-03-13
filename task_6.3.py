from itertools import zip_longest
import json

users = []
hobbys = []
user_hobby = {}

with open('users.csv', encoding='utf-8') as u:
   for i in u:
       rez = str(i.replace(',', ' ').replace('\n', ''))
       users.append(rez)

with open('hobby.csv', encoding='utf-8') as h:
    for i in h:
        hob = str(i.replace('\n', ''))
        hobbys.append(hob)

if len(users) > len(hobbys):
    user_hobby = {(name, hobby) for (name, hobby) in zip_longest(users, hobbys, fillvalue=None)}
    dict_in_json = json.dumps(user_hobby, ensure_ascii=False)
    with open('rez_6.3.json', 'w', encoding='utf-8') as r:
        r.write(dict_in_json)
else:
    for i in range(len(users)):
        user_hobby[users[i]] = hobbys[i]
        dict_in_json = json.dumps(user_hobby, ensure_ascii=False)

        with open('rez_6.3.json', 'w', encoding='utf-8') as r:
            r.write(dict_in_json)
    exit(1)
