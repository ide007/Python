def bakery_in(chek):
    with open('bakery.csv', 'a', encoding='utf-8') as bak:
        num = (str(float(chek)))
        bak.write(num  + '\n')
        print('чек оплачен')
    return ''


if __name__ == '__main__':
    from sys import argv
    print(bakery_in(argv[1]))
