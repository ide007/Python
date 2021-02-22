# A (Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.)
# B Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
price_list = [57.8, 46.51, 97, 12.05, 73.5, 31, 25.13, 64.9, 86.09, 7.17, 0.5, 99.9]
print(price_list)
print(id(price_list))
price_list.sort()
for idx, value in enumerate(price_list):
    rubl = int(value)
    kop = round((value - rubl) * 100)
    if len(str(kop)) < 2:
        kop = str(kop).zfill(2)
    print(f'{rubl} руб {kop} коп', end=', ')
print('\n',id(price_list))
# C (Создать новый список, содержащий те же цены, но отсортированные по убыванию.)
price_list_reverse = sorted(price_list, reverse=True)
print(price_list_reverse)
for idx, value in enumerate(price_list_reverse):
    rubl = int(value)
    kop = round((value - rubl) * 100)
    if len(str(kop)) < 2:
        kop = str(kop).zfill(2)
    print(f'{rubl} руб {kop} коп', end=', ')
print('\n', id(price_list_reverse))
# D Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию,
# написав минимум кода? Да (2 строки)
for idx, value in enumerate(sorted(sorted(price_list, reverse=True)[0:5:])):
    print(f'{int(value)} руб {str(round((value - int(value)) * 100)).zfill(2)} коп', end=', ')
