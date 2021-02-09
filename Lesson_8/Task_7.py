class Complex:
    def __init__(self, real_num, imaginary_unit=0):
        self.real_num = real_num
        self.imaginary_unit = imaginary_unit

    def __add__(self, other):
        return Complex(self.real_num + other.real_num, self.imaginary_unit + other.imaginary_unit)

    def __mul__(self, other):
        return Complex(self.real_num * other.real_num - self.imaginary_unit * other.imaginary_unit,
                       self.real_num * other.imaginary_unit + other.real_num * self.imaginary_unit)

    def __str__(self):
        if self.imaginary_unit < 0:
            return f'({self.real_num}{self.imaginary_unit}j)'
        else:
            return f'({self.real_num}+{self.imaginary_unit}j)'


a = Complex(1, 3)
b = Complex(5, -2)
print(a)
print(complex(1, 3))
print()

print(b)
print(complex(5, -2))
print()

print(a + b)
print(complex(1, 3) + complex(5, -2))
print()

print(a * b)
print(complex(1, 3) * complex(5, -2))
