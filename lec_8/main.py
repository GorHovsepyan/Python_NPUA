class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def set_value(self, row, col, value):
        if 0 <= row < self.n and 0 <= col < self.m:
            self.matrix[row][col] = value
        else:
            print("Invalid row or column index.")

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total_sum = sum(sum(row) for row in self.matrix)
        mean = total_sum / (self.n * self.m)
        return mean

    def calculate_row_sum(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            print("Invalid row index.")
            return None

    def calculate_column_average(self, col_index):
        if 0 <= col_index < self.m:
            total = sum(row[col_index] for row in self.matrix)
            average = total / self.n
            return average
        else:
            print("Invalid column index.")
            return None

    def print_submatrix(self, col1, col2, row1, row2):
        if 0 <= col1 < col2 <= self.m and 0 <= row1 < row2 <= self.n:
            for row in self.matrix[row1:row2]:
                print(row[col1:col2])
        else:
            print("Invalid submatrix indices.")


n = 3
m = 4
matrix = Matrix(n, m)

for i in range(n):
    for j in range(m):
        matrix.set_value(i, j, i * m + j)

matrix.print_matrix()
print("Mean of the matrix:", matrix.calculate_mean())
row_index = 1
print(f"Sum of row {row_index}:", matrix.calculate_row_sum(row_index))
col_index = 2
print(f"Average of column {col_index}:", matrix.calculate_column_average(col_index))
col1, col2, row1, row2 = 1, 3, 0, 2
print("Submatrix:")
matrix.print_submatrix(col1, col2, row1, row2)
