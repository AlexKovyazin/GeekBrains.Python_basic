my_list = [int(i) for i in input('Введите содержимое списка через пробел: ').split(' ')]
for i in my_list[0::2]:
    if len(my_list) % 2 == 1:
        if i == len(my_list) - 1:
            break
    if i == len(my_list):
        break
    my_list.insert(i - 1, my_list.pop(i))
print(my_list)
