def division(dividend, divisor):
    """Выводит в консоль результат деления dividend на divisor"""
    try:
        div_result = int(dividend) / int(divisor)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        pass
    except ValueError:
        print('Неверные аргументы!')
        pass
    else:
        print(div_result)


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
division(num_1, num_2)
