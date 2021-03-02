from requests import get, utils
from datetime import date


def currency_rate(currency):
    currency = currency.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    endcodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=endcodings)
    date_req = (content[content.find('Date') + 6: (content.find('Date')) + 16:])
    if currency not in content:
        print('None')
    else:
        slice_val = (content[content.find(currency): (content.find(currency)) + 85:])
        value = slice_val.replace('</', ' ').replace('>', ' ').replace(',', '.').replace('<', ' ').split()
        kurs = []
        for val in value:
            if val.isalpha() != True:
                kurs.append(val)
        kurs[1] = float(kurs[1])
        print('Дата запроса :', date_req)
        print('Курс :', (kurs[0]), (currency), ' = ', "{0:.2f} RUB".format(kurs[1]))


currency_rate(input('курс какой валюты хотите узнать? :'))

