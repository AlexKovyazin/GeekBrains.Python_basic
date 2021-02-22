from abc import abstractmethod


class Storage:
    counter = 3
    model_list = ['Canon IR 3520', 'Canon CanonScan LiDE 300', 'Xerox test']
    storage_list = [('Canon IR 3520', {'type': 'printer',
                                       'amount': 15,
                                       'print_tech': 'laser',
                                       'paper_size': 'a3',
                                       'is_color': 'color'}),
                    ('Canon CanonScan LiDE 300', {'type': 'scanner',
                                                  'amount': 8,
                                                  'type_of_scan': 'flatbed',
                                                  'paper_size': 'a4'}),
                    ('Xerox test', {'type': 'copier',
                                    'amount': 12,
                                    'paper_size': 'a3'})]

    def __init__(self, capacity):
        self.capacity = capacity

    @staticmethod
    def remove():
        """Удаляет из склада выбранную технику"""
        del_model = input('Введите модель, которую хотите удалить со склада: ')
        while True:
            try:
                amount_of_del = int(input('Введите количество единиц, которое необходимо удалить: '))
                break
            except ValueError:
                print('Необходимо ввести число!')

        try:
            Storage.model_list.index(del_model)  # Проверка на то, есть ли указанная модель на складе
        except ValueError:
            print('Указанная вами модель не найдена на складе!\n')

        for tup in Storage.storage_list:
            if tup[0] == del_model:  # Поиск модели в кортежах списка storage_list
                if tup[1]['amount'] < amount_of_del:  # Если кол-во единиц на складе меньше удаляемого
                    del_confirm = int(input('Вы хотите удалить большее кол-во единиц чем имеется на складе!\n'
                                            'Удалить все единицы указанной модели?\n'
                                            '(1 - Удалить все единицы указанной модели, '
                                            '2 - Прервать операцию удаления): '))
                    if del_confirm == 1:
                        Storage.storage_list.remove(tup)
                        Storage.model_list.remove(del_model)
                        print(f'\nвсе единицы модели {del_model} удалены со склада\n')
                    elif del_confirm == 2:
                        print(f'\nОперация удаления модели {del_model} отменена\n')
                        break
                elif tup[1]['amount'] == amount_of_del:  # Если кол-во единиц на складе равняется удаляемому
                    Storage.storage_list.remove(tup)
                    Storage.model_list.remove(del_model)
                    print(f'Модель {del_model} удалена со склада\n')
                    break
                elif tup[1]['amount'] > amount_of_del:  # Если кол-в единиц на складе больше удаляемого
                    tup[1]['amount'] = tup[1]['amount'] - amount_of_del
                    print(f'{amount_of_del} единиц модели {del_model} удалено со склада\n')
                    break
            else:
                continue

    @staticmethod
    def table(type_of_office_equipment):
        """Выводит табличное представление заполнения склада по заданному типу техники"""
        result_list = []
        # Создание матрицы необходимого размера (принтер).
        if type_of_office_equipment.lower() == 'printer':
            result_list = [[0 for i in range(6)] for j in range(len(Storage.storage_list))]
        elif type_of_office_equipment.lower() == 'scanner':
            result_list = [[0 for i in range(5)] for j in range(len(Storage.storage_list))]
        elif type_of_office_equipment.lower() == 'copier':
            result_list = [[0 for i in range(4)] for j in range(len(Storage.storage_list))]
        else:
            return print('Введён неправильный тип данных!')

        # Добавление первой строки с характеристиками.
        if type_of_office_equipment.lower() == 'printer':
            result_list.insert(0, ['model', 'type', 'amount', 'print tech', 'paper size', 'is color'])
        elif type_of_office_equipment.lower() == 'scanner':
            result_list.insert(0, ['model', 'type', 'amount', 'type_of_scan', 'paper size'])
        elif type_of_office_equipment.lower() == 'copier':
            result_list.insert(0, ['model', 'type', 'amount', 'paper size'])

        # Заполнение строк характеристиками
        for i in range(1, len(Storage.storage_list) + 1):
            if Storage.storage_list[i - 1][1]['type'] == type_of_office_equipment.lower():
                # Вносим модель в первый столбец
                result_list[i][0] = Storage.storage_list[i - 1][0]
                for j in range(1, len(Storage.storage_list[i - 1][1].keys()) + 1):
                    # Заполнение строки по ключу полученному из списка dict.keys(), где:
                    # Storage.storage_list[i - 1] - tuple
                    # Storage.storage_list[i - 1][1] - dict
                    # list(Storage.storage_list[i - 1][1].keys()) - список ключей из dict
                    # str(list(Storage.storage_list[i - 1][1].keys())[j - 1]) -
                    # строковое представление житого ключа в списке ключей
                    result_list[i][j] = Storage.storage_list[i - 1][1][
                        str(list(Storage.storage_list[i - 1][1].keys())[j - 1])]

        # Очищаем result_list от пустых строк
        intermediate_list = []
        for i in result_list:
            try:
                if sum(i) == 0:
                    continue
            except TypeError:  # Если в списке есть отличные от нуля значения, то их не получится сложить
                intermediate_list.append(i)
        result_list = intermediate_list

        # Вывод на печать таблицы
        for lst in result_list:
            for el in lst:
                print(str(el).ljust(25), end='\t')
            print()
        print()


class OfficeEquipment:

    def __init__(self, model, amount, paper_size):
        self.model = model
        self.amount = amount
        self.paper_size = paper_size

    @abstractmethod
    def add_to_storage(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, model, amount, print_tech, paper_size, is_color):
        super().__init__(model, amount, paper_size)
        self.print_tech = print_tech
        self.is_color = is_color

    def add_to_storage(self):
        Storage.storage_list.append((self.model, {'type': 'printer',
                                                  'amount': self.amount,
                                                  'print_tech': self.print_tech,
                                                  'paper_size': self.paper_size,
                                                  'is_color': self.is_color}))
        Storage.model_list.append(self.model)
        Storage.counter += 1
        print(f'Модель {self.model} в количестве {self.amount} ед. добавлена на склад\n'
              f'Идентификационный номер - p-{Storage.counter}\n')


class Scanner(OfficeEquipment):

    def __init__(self, model, amount, type_of_scan, paper_size):
        super().__init__(model, amount, paper_size)
        self.type_of_scan = type_of_scan

    def add_to_storage(self):
        Storage.storage_list.append((self.model, {'type': 'scanner',
                                                  'amount': self.amount,
                                                  'type_of_scan': self.type_of_scan,
                                                  'paper_size': self.paper_size}))
        Storage.model_list.append(self.model)
        Storage.counter += 1
        print(f'Модель {self.model} в количестве {self.amount} ед. добавлена на склад\n'
              f'Идентификационный номер - s-{Storage.counter}\n')


class Copier(OfficeEquipment):

    def __init__(self, model, amount, paper_size):
        super().__init__(model, amount, paper_size)

    def add_to_storage(self):
        Storage.storage_list.append((self.model, {'type': 'copier',
                                                  'amount': self.amount,
                                                  'paper_size': self.paper_size}))
        Storage.model_list.append(self.model)
        Storage.counter += 1
        print(f'Модель {self.model} в количестве {self.amount} ед. добавлена на склад\n'
              f'Идентификационный номер - c-{Storage.counter}\n')


#############################################

storage = Storage(400)
a = Printer('Canon 123', 13, 'laser', 'a4', 'color')
b = Scanner('Test Scanner', 32, 'какой-то тип', 'A2')
c = Copier('Test Copier', 40, 'A4')
a.add_to_storage()
b.add_to_storage()
c.add_to_storage()

print('Начало работы со складом')

while True:
    while True:
        try:
            print('Возможные действия:\n'
                  '1 - Посмотреть сводные таблицы по имеющимся на складе категориям (принтер, сканнер, копир)\n'
                  '2 - Добавить товары на склад\n'
                  '3 - Удалить товары со склада')
            mode = int(input('Для продолжения введите цифру соответстующую необходимому действию: '))
            print()
            break
        except ValueError:
            print('Необходимо ввести число 1, 2 или 3!')

    # Я больше не хочу защищать всё от дураков. Это можно делать бесконечно, но задача ведь не об этом
    if mode == 1:
        type_of_equipment_to_table = int(input('Введите тип техники по которому хотите получить сводную таблицу\n'
                                               '(1 - принтер, 2 - сканнер, 3 - копир): '))
        print()
        if type_of_equipment_to_table == 1:
            Storage.table('printer')
        elif type_of_equipment_to_table == 2:
            Storage.table('scanner')
        elif type_of_equipment_to_table == 3:
            Storage.table('copier')

    elif mode == 2:
        type_of_equipment_to_add = int(input('Введите тип техники который хотите добавить на склад\n'
                                             '(1 - принтер, 2 - сканнер, 3 - копир): '))
        if type_of_equipment_to_add == 1:
            p_model = input('Введите модель техники: ')
            p_type = 'printer'
            p_amount = int(input('Сколько единиц техники будет добавлено на склад?: '))
            p_print_tech_num = int(input('Тип печати\n'
                                         '(1 - laser, 2 - inkjet): '))
            if p_print_tech_num == 1:
                p_print_tech = 'laser'
            else:   # знаю, что так любые значения p_print_tech_num будут попадать сюда, но я не завхоз на этом складе)
                p_print_tech = 'inkjet'
            p_paper_size = input('Введите допустимый формат бумаги\n'
                                 '(A0, A1, A2, A3, A4: ')
            p_is_color = input('Поддерживается ли цветная печать?\n'
                               '(да - color, нет - black/white): ')
            print()
            Printer(p_model, p_amount, p_print_tech, p_paper_size, p_is_color).add_to_storage()
        elif type_of_equipment_to_add == 2:
            s_model = input('Введите модель техники: ')
            s_type = 'scanner'
            s_amount = int(input('Сколько единиц техники будет добавлено на склад?: '))
            type_of_scan_num = int(input('Тип сканера\n'
                                         '(1 - flatbed, 2 - Sheetfed): '))
            if type_of_scan_num == 1:
                s_type_of_scan = 'flatbed'
            else:   # знаю, что так любые значения p_print_tech_num будут попадать сюда, но я не завхоз на этом складе)
                s_type_of_scan = 'Sheetfed'
            s_paper_size = input('Введите допустимый формат бумаги\n'
                                 '(A0, A1, A2, A3, A4: ')
            print()
            Scanner(s_model, s_amount, s_type_of_scan, s_paper_size).add_to_storage()
        elif type_of_equipment_to_add == 3:
            c_model = input('Введите модель техники: ')
            c_type = 'copier'
            c_amount = int(input('Сколько единиц техники будет добавлено на склад?: '))
            c_paper_size = input('Введите допустимый формат бумаги\n'
                                 '(A0, A1, A2, A3, A4: ')
            print()
            Copier(c_model, c_amount, c_paper_size).add_to_storage()

    elif mode == 3:
        Storage.remove()

    repeat = int(input('Вызвать меню?\n'
                       '(1 - вызвать меню, 2 - выход): '))
    print()
    if repeat == 1:
        continue
    if repeat == 2:
        print('Завершение работы')
        break
