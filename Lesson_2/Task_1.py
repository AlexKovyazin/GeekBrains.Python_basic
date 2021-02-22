my_list = [1, 'my_string', [1, 2, 3], ('my_tuple', 1, 2), {'my_dict': 12}, None, True]
for index, item in enumerate(my_list):
    print(f'Элемент списка № {index + 1} - {type(item)}')
    if isinstance(item, (list, dict, tuple, type)) is True:
        print(f'Содержит в себе несколько объектов. Разворачиваю сожержимое:')
        for in_index, in_item in enumerate(my_list[index]):
            print(f'    Объект № {in_index + 1} - {type(in_item)}')
