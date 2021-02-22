class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
print('Введите числа для добавления в список (не числовые значения не будут добавлены!)')
while True:
    element = input("Введите число (для завершения введите 'stop'): ")
    if element == 'stop':
        print(result_list)
        break
    else:
        try:
            result_list.append(float(element))
            print(f'В список добавлено число {float(element)}')
        except ValueError:
            print('Необходимо вводить только числа!')
            continue
