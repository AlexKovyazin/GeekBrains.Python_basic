def func_time(x):
    if x < 10:
        return '0' + str(x)
    else:
        return str(x)

# через 10 минут поисков методов добавления нуля перед значением при помощи
# f строк я сдался и ради экономии места пришлось сделать так


sec = int(input('Введите количество секунд: '))
hours = sec // 3600
minutes = sec // 60 - hours * 60
seconds = sec % 60
print(f'{func_time(hours)}:{func_time(minutes)}:{func_time(seconds)}')
