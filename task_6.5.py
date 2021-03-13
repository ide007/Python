def bakery(users, hobbys, rezult):
    with open(users, encoding='utf-8') as u, open(hobbys, encoding='utf-8') as h:
       for i in u:
           if h.readline().endswith('\n'):
               rez = str(i.replace(',', ' ').replace('\n', '') + ': ' + h.readline().replace('\n', ''))
               with open(rezult, 'a', encoding='utf-8') as r:
                   r.write(rez + '\n')
               if not i.endswith('\n'):
                  exit(1)
           else:
               rez = str(i.replace(',', ' ').replace('\n', '') + ': None')
               with open(rezult, 'a', encoding='utf-8') as r:
                   r.write(rez + '\n')


if __name__ == '__main__':
    from sys import argv

    users, hobbys, rezult = argv[1:]
    bakery(*argv[1:])
