import random

matrix_1 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(-100, 100))  
    matrix_1.append(row)

matrix_2 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(-100, 100))  
    matrix_2.append(row)

matrix_3 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_3.append(row)

print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nМатрица 3 (сумма):")
for row in matrix_3:
    print(row)