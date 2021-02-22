with open('Task_1.txt', 'w', encoding='utf-8') as t1:
    while True:
        user_str = input('Введите вашу строку: ')
        if user_str == '':
            break
        else:
            print(user_str, file=t1)
