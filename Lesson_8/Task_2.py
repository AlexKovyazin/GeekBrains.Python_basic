class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        first_num = int(input('Введите делимое: '))
        second_num = int(input('Введите делитель: '))
        if second_num == 0:
            raise MyError('Делитель не может быть равен нулю!')
        else:
            break
    except MyError as err:
        print(err)

print(first_num / second_num)




