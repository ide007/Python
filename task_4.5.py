from requests import get, utils

def currency_rate(curr):
    curr = curr.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    endcodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=endcodings)
    date = (content[content.find('Date') + 6: (content.find('Date')) + 16:])
    if curr not in content:
        print('None')
    else:
        slice_val = (content[content.find(curr): (content.find(curr)) + 85:])
        value = slice_val.replace('</', ' ').replace('>', ' ').replace(',', '.').replace('<', ' ').split()
        kurs = []
        for val in value:
            if val.isalpha() != True:
                kurs.append(val)
        kurs[1] = float(kurs[1])
        print('Дата запроса :', date)
        print('Курс :', (kurs[0]), (curr), ' = ', "{0:.2f} RUB".format(kurs[1]))
    return ''

if __name__ == '__main__':
    from sys import argv
    print(currency_rate(argv[1]))
