num = input('Введите целое положительное число: ')
max_num = num % 10
while num != 0:
    if num % 10 > max_num:
        max_num = num % 10
    else:
        num = num // 10
print(max_num)
