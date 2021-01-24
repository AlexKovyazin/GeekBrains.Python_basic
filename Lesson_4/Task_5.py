from functools import reduce


def multiplication(your_list):
    """Перемножет все элементы списка и выводит результат умножения"""
    result = 1
    for num in your_list:
        result *= num
    return result


my_list = [num for num in range(100, 1001)]

# проверка через функцию multiplication

print(multiplication(my_list))

# проверка через лямбда функцию

print(reduce(lambda x, y: x * y, my_list))
