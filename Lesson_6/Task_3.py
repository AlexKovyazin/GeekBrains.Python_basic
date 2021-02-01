import random


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income['wage'], 'bonus': income['bonus']}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position('Alex', 'White', 'engineer', {'wage': round(random.randint(10000, 100000), 3),
                                                  'bonus': round(random.randint(10000, 100000))})
worker_2 = Position('Tom', 'Brown', 'designer', {'wage': round(random.randint(10000, 100000), 3),
                                                 'bonus': round(random.randint(10000, 100000))})

print(f'{worker_1.get_full_name()} - {worker_1.get_total_income()}')
print(f'{worker_2.get_full_name()} - {worker_2.get_total_income()}')

