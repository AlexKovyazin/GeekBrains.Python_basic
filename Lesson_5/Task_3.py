salary_dict = {}
with open('salary.txt', 'r', encoding='utf-8') as salary_txt:
    for line in salary_txt.readlines():

        # делаем срез строки с начала до символа "-"
        name = line[:line.find('-')]

        # делаем срез строки с символа "-" до конца строки;
        # приводим строку к int
        salary = int(line[line.find('-') + 1:len(line)])
        salary_dict[name] = salary

print('Сотрудники, заработная плата которых менее 20000:')
for worker, sal in salary_dict.items():
    if sal < 20000:
        print(f'\t{worker} - {sal}')

print(f'Средняя заработная плата всех сотрудников - {(sum(salary_dict.values())) / len(salary_dict)}')
