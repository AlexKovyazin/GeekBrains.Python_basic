from functools import reduce


def multiplication(stop_num):
    """Перемножет все элементы списка и выводит результат умножения"""

    # то же самое, что в задаче № 5, но импортировать только функцию multiplication не получилось -
    # - выдавал ещё и результат всей задачи № 5.
    # Надо сделать условие с name и __main__?

    result_list = []
    for i in range(1, stop_num + 1):
        result_list.append(i)
    return reduce(lambda x, y: x * y, result_list)


def fact_yield(stop_num):
    for element in (multiplication(num) for num in range(1, stop_num + 1)):
        yield element


for el in fact_yield(20):
    print(el)
