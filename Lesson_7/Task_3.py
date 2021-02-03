class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if (self.amount - other.amount) > 0:
            return Cell(self.amount - other.amount)
        else:
            return 'Разность переданных аргументов меньше 0. Операция невозможна'

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(round(self.amount // other.amount))

    def make_order(self, in_a_row):
        self.in_a_row = in_a_row
        num_of_rows = self.amount // in_a_row
        result = ''
        for i in range(num_of_rows):
            result += in_a_row * '*'
            result += '\n'
        result += self.amount % in_a_row * '*'
        return result

    def __str__(self):
        return str(self.amount * '*')


a = Cell(5)
b = Cell(10)
c = Cell(12)
d = a + b

print(
  f'a - {a}\n'
  f'b - {b}\n'
  f'c - {c}\n'
  f'd - {d}\n'
  f'(a + b + c) - {a + b + c}\n'
  f'(a - b) - {a - b}\n'
  f'(b - a) - {b - a}\n'
  f'(a * b) - {a * b}\n'
  f'(c / a) - {c / a}\n'
  f'(a + b + c) - Представление выражения дано ниже:\n{(a + b + c).make_order(4)}\n')
