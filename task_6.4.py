with open('users.csv', encoding='utf-8') as u, open('hobby.csv', encoding='utf-8') as h:
   for i in u:
       if h.readline().endswith('\n'):
           rez = str(i.replace(',', ' ').replace('\n', '') + ': ' + h.readline().replace('\n', ''))
           with open('rez_6.3.txt', 'a', encoding='utf-8') as r:
               r.write(rez + '\n')
           if not i.endswith('\n'):
              exit(1)
       else:
           rez = str(i.replace(',', ' ').replace('\n', '') + ': None')
           with open('rez_6.3.txt', 'a', encoding='utf-8') as r:
               r.write(rez + '\n')
