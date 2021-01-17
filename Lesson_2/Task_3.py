seasons_dict = {'зима': (12, 1, 2),
                'весна': (3, 4, 5),
                'лето': (6, 7, 8),
                'осень': (9, 10, 11)}

seasons_list = [['зима', 12, 1, 2],
                ['весна', 3, 4, 5],
                ['лето', 6, 7, 8],
                ['осень', 9, 10, 11]]

while True:
    month = input('Введите ваш месяц в виде числа: ')
    if month.isalpha() is True:
        print('Введите число от 1 до 12')
        continue
    if int(month) > 12 or int(month) <= 0:
        print('Введите число от 1 до 12')
    else:
        month = int(month)
        break


print('Проверка через словарь...')
for keys in seasons_dict:
    if seasons_dict[keys].count(month) == 1:
        print(f'Месяц № {month} это {keys}')

print('Проверка через список...')
for i in range(0, 4):
    for j in range(1, 3):
        if seasons_list[i][j] == month:
            print(f'Месяц № {month} это {seasons_list[i][0]}')
            break
