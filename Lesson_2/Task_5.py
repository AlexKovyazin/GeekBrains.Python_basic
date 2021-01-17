my_list = [7, 5, 3, 3, 2]
condition_to_continue = None
while condition_to_continue != 'нет':
    new_num = input('Введите ваше число: ')
    if not new_num.isdigit():
        print('необходимо ввести число!')
        continue
    my_list.append(int(new_num))
    my_list.sort()
    print(my_list)
    while condition_to_continue != 'нет':
        condition_to_continue = input('Хотите добавить еще числа? (да/нет): ')
        if condition_to_continue == 'да':
            break
        elif condition_to_continue == 'нет':
            print(f'Итоговый рейтинг: {my_list}')
            break
        else:
            print('Вы ввели что-то неведомое. Введите "да" или "нет"')
            continue
