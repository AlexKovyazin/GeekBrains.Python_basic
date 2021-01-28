discipline_dict = {}
with open('Task_6.txt', encoding='utf-8') as task_6:
    for line in task_6.readlines():

        # добавляем в словарь ключ с названием предмета
        discipline = line[:line.find(':')]

        # разбиваем line на части
        line_list = line.split(' ')
        # в line_list накапливаем цифры в строковом формате и конкатенируем их
        line_intermediate_str = ''
        # пустой список для накопления цифровых значений из строки
        hours = []

        # вычленяем цифры из каждого слова в строке и добавляем их в строковом виде в hours после конкатенации
        for part in line_list:
            for char in part:
                if not char.isdigit():
                    continue
                else:
                    line_intermediate_str += char
            hours.append(line_intermediate_str)
            line_intermediate_str = ''

        # убираем из списка пустые значения и приводим оставшиеся значения к int

        # !!! изначально ошибочно ввёл не существующее в пространстве имён наименование
        # и при это всё равно получил верный результат. Как это получилось? !!!
        
        hours = [int(value) for value in hours if value]
        # добавляем в discipline_dict полученное наименование предмета и суммарное количество часов
        discipline_dict[discipline] = sum(hours)
print(discipline_dict)
