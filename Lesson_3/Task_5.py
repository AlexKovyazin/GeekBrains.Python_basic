intermediate_sum = 0
condition_to_continue = True
while condition_to_continue is True:
    num_str = [i for i in input('Введите числа через пробел: ').split()]
    for num in num_str:
        if 48 <= ord(str(num)) <= 57:
            intermediate_sum += int(num)
        else:
            condition_to_continue = False
            break
    print(intermediate_sum)
