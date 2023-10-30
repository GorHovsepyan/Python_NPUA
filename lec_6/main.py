import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    column_sum = sum(row[column_index] for row in matrix)
    return column_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = generate_random_matrix(rows, cols)

print("Generated Matrix:")
for row in matrix:
    print(row)

column_index = int(input("Enter the column index to get the sum: "))
column_sum = get_column_sum(matrix, column_index)
print(f"Sum of column {column_index}: {column_sum}")

row_index = int(input("Enter the row index to get the average: "))
row_average = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {row_average}")
