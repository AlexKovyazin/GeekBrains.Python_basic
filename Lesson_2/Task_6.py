my_list = []    # Список для внесения данных пользовтелем
my_dict = {}    # Словарь для сбора аналитики
counter = 0     # Счётчик для нумерации товров
condition_to_continue = None    # Условие для добавления новых товаров

# Наполнение списка пользователем

while condition_to_continue != 'нет':
    product = input('Введите наименование товара: ')
    price = input('Введите цену товара: ')
    quantity = input('Введите количество товара: ')
    units = input('Введите единицы измерения: ')
    my_list.append((counter + 1, {'название': product, 'цена': price, 'количество': quantity, 'ед.': units}))

# Проверка необходимости добавления еще одного товара:

    while condition_to_continue != 'нет':
        condition_to_continue = input('Хотите добавить ещё товары? (да/нет): ')
        if condition_to_continue == 'да':
            break
        elif condition_to_continue == 'нет':
            break
        else:
            print('Вы ввели что-то неведомое. Введите "да" или "нет"')
            continue
    counter += 1

#   добавляем в итоговый словарь аналитики имеющиеся характеристики товаров:

for tup, dic in my_list:
    for key in dic:
        my_dict.setdefault(key, [])
        my_dict[key].append(dic.get(key))
print('Вот ваша аналитика:')
print(my_dict)
