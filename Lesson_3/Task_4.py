def my_func(x, y):
    """Возводит аргумент x в степень y, где y - отрицательное число"""
    try:
        # Проверка на то, что один из аргументов не является числом

        type_test = x % y

    # Следующий except является защитой от строки № 6 при условии, что y = 0
    # (понимаю, что можно было обойтись без try except, но мы всё-таки их только прошли и хотелось попробовать везде)

    except ZeroDivisionError:
        return 1
    except TypeError:
        print('Неверный тип данных!')
        return None
    if y > 0:
        print('Аргумент y должен быть <0!')
        return None
    else:
        y = -y
        my_list = [x] * y
        result = x
        for i in range(0, len(my_list) - 1):
            result *= my_list[i]
        return 1 / result


print(my_func(2, 2))
