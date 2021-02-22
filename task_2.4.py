basic_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for idx, value in enumerate(basic_list):
    _ = value.split()
    print(f'Привет, {_[-1].title()}! ')
