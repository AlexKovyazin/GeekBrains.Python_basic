class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.counter = 0

    # Итератор не пригодился

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     if self.counter < len(self.matrix):
    #         self.counter += 1
    #         return self.matrix[self.counter - 1]
    #     else:
    #         raise StopIteration

    def __str__(self):
        result = ""
        for row in self.matrix:
            for num in row:
                result += f'{num:<3}'
            result += "\n"
        return result

    def __add__(self, other):
        result = [[0] * (len(self.matrix) - 1) for _ in range(len(self.matrix))]
        for row_index in range(len(other.matrix)):
            for num_index in range(len(other.matrix[row_index])):
                result[row_index][num_index] += (self.matrix[row_index][num_index] + other.matrix[row_index][num_index])
        return Matrix(result)


a = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
b = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]])
c = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]])
print(a + b + c)
print(a, b, c, sep='\n')
