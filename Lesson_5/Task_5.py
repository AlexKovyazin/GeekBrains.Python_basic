with open('Task_5.txt', 'w+', encoding='utf-8') as txt:
    txt.write(input('Введите числа, разделённые пробелами: '))
    txt.seek(0)
    numbers_str = txt.read().split(' ')
numbers = []
for num in numbers_str:
    numbers.append(int(num))
print(sum(numbers))
