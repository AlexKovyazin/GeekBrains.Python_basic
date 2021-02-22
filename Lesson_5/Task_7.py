import json


comp_profit_dict = {}
average_profit_dict = {}
comp_list = []
result_list = []

with open('text_7.txt', encoding='utf-8') as txt:
    # Преобразуем строки из txt в элементы списка (comp_list) разделённые через split
    for line in txt.readlines():
        comp_list.append(line.split(' '))

# заполняем словарь с прибылью фирм (comp_profit_dict)
for company in comp_list:
    comp_profit_dict[company[0]] = int(company[2]) - int(company[3])

# заполняем список intermediate_profit_list для дальнейшего вычисления средней прибыли
intermediate_profit_list = []
profit_companies = 0
for key, value in comp_profit_dict.items():
    if value > 0:
        intermediate_profit_list.append(value)
        profit_companies += 1
    else:
        continue
# добавляем в словарь average_profit_dict значение средней прибыли компаний, которые её имеют
average_profit_dict['average_profit'] = sum(intermediate_profit_list) / profit_companies

# заполняем итоговый список
result_list = [comp_profit_dict, average_profit_dict]
print(result_list)

# записываем итоговый список в json файл
with open('text_7.json', 'w', encoding='utf-8') as txt_json:
    json.dump(result_list, txt_json, ensure_ascii=False, indent='\t')
