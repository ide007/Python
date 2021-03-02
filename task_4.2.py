from requests import get, utils


def currency_rate(currency):
    currency = currency.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    endcodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=endcodings)
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
        print('Курс :', (kurs[0]), (currency), ' = ', "{0:.2f} RUB".format(kurs[1]))


currency_rate(input('курс какой валюты хотите узнать? :'))
currency_rate('USD')
currency_rate('EUR')
