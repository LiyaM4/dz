# Задание 1
N = int(input("Введите кол-во строк: "))
num = [int(input("Введите число: ")) for _ in range(N)]

rever_num = num[::-1]

for num in rever_num:
    print(num)
    
# Задание 2
def a(x):
    return x[::-1]

N1 = int(input("Введите число N: "))
num1 = list(map(int, input("Введите N чисел через пробел: ").split()))

result = a(num1)
for num1 in result:
    print(num1, end=' ')
    
    
# Задание 3
def min_1(m, n, weights):
    weights.sort()
    boats = 0
    left, right = 0, n - 1

    while left <= right:
        if left == right:
            boats += 1
            break
        if weights[left] + weights[right] <= m:
            left += 1
        right -= 1
        boats += 1

    return boats

m = int(input("Введите максимальную массу: "))
n = int(input("Введите количество рыбаков: "))
weights = [int(input("Введите вес рыбака: ")) for _ in range(n)]

result = min_1(m, n, weights)
print(result)