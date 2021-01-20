def my_func(num_1, num_2, num_3):
    """Возвращает сумму двух максимальных чисел из args"""
    my_func_tuple = (num_1, num_2, num_3)
    try:
        sum_of_2_max = sum(my_func_tuple) - min(my_func_tuple)
    except TypeError:
        print('Неверный тип данных!')
        pass
    else:
        return sum_of_2_max


a = 1
b = 2
c = 3
x = 'str'

print(my_func(a, b, c))
print(my_func(a, b, x))
