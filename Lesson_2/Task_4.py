my_list = input('Введите слова через пробел: ').split(' ')
for ind, value in enumerate(my_list):
    if len(value) > 10:
        print(f'{ind + 1}-{value[:10]}')
    else:
        print(f'{ind + 1}-{value}')
