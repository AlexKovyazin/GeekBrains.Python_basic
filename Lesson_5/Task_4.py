num_dict = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре'}
trans_dict = {}
ru_dict = {}
with open('Task_4.txt', encoding='utf-8') as txt:
    for line in txt.readlines():
        print(line)
        print(line.find(' '))
        alpha_num = line[0:line.find(' ')]
        digit_num = line[line.find(' ') + 3: len(line) - 1]
        trans_dict[alpha_num] = digit_num
print(trans_dict)
for key, value in trans_dict.items():
    # берём ключи из trans_dict, делаем их строчными буквами, ищем их в num_dict,
    # значения из num_dict делаем с первой заглавной буквой
    # и создаём такой ключ в ru_dict присваивая значения value из trans_dict
    ru_dict[num_dict[key.lower()].title()] = value
print(ru_dict)
with open('Task_4_result.txt', 'w', encoding='utf-8') as result:
    for key, value in ru_dict.items():
        print(f'{key} - {value}', file=result)
