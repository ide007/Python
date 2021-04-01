class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def dat_to_num(cls, data):
        try:
            rez = []
            for num in cls.valid(data):
                rez.append(int(num))
            return f"число: {rez[0]} месяц: {rez[1]} год: {rez[2]}"
        except ValueError:
            return 'Неправильный формат даты!'

    @staticmethod
    def valid(data):
        date = data.split('-')
        day, month, year = date
        if 0 < int(day) <= 31 and 0 < int(month) <= 12 and 1900 < int(year) < 2030:
            return date
        else:
            return ValueError


print(Data.dat_to_num('30-03-2000'))
print(Data.dat_to_num('23-авг-2000'))
