proceeds = int(input('Введите вашу выручку: '))
costs = int(input('Введите ваши издержки: '))
if proceeds < costs:
    print('Убыток(')
elif proceeds == costs:
    print('вы работаете в ноль')
else:
    print('Прибыль')
    print(f'Рентабельность выручки {proceeds / costs}')
    staff = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет {proceeds / costs / staff}')
