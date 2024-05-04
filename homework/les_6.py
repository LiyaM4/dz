# Задача 1
N = int(input("Введите количество чисел: "))
k = 0

for a in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        k += 1

print("Количество нулей:", k)

# Задача 2
X = int(input("Введите натуральное число: "))
def count_1(X):
    с = 0
    i = 1
    while i * i <= X:
        if X % i == 0:
            с += 2
            if i * i == X:
                с -= 1
        i += 1
    return с

print("Количество делителей:", count_1(X))

# Задача 3
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

for i in range(A, B+1):
    if i % 2 == 0:
        print(i, end=" ")
