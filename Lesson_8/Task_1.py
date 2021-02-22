class Date:
    def __init__(self, txt):
        self.txt = txt
        self.day = txt.split('-')[0]
        self.month = txt.split('-')[1]
        self.year = txt.split('-')[2]
        Date.transformation(self)

    @classmethod
    def transformation(cls, date_obj):
        date_obj.day = int(date_obj.day)
        date_obj.month = int(date_obj.month)
        date_obj.year = int(date_obj.year)

    @staticmethod
    def validate(date_obj):
        if not 1 <= date_obj.day <= 31:
            print('Значение day должно быть в пределах от 1 до 31')
        if not 1 <= date_obj.month <= 12:
            print('Значение month должно быть в пределах от 1 до 12')
        if not 0 <= date_obj.year <= 9999:
            print('Значение year должно быть в пределах от 1 до 9999')
        if 1 <= date_obj.day <= 31 and 1 <= date_obj.month <= 12 and 0 <= date_obj.year <= 9999:
            print('Проверка прошла успешно!')


a = Date('12-02-2020')
print(a.txt)
print(f'{a.day} - {type(a.day)}')
print(f'{a.month} - {type(a.month)}')
print(f'{a.year} - {type(a.year)}')
a.validate(a)
print()

b = Date('32-13-2020')
print(b.txt)
b.validate(b)
