# Задание 1
N = int(input("Введите количество чисел: "))
num = list(map(int, input("Введите числа через пробел: ").split()))

tmp = set(num)
c = len(tmp)

print(c)

# Задание 2
num = set(map(int, input("Введите числа через пробел: ").split()))
num2 = set(map(int, input("Введите числа через пробел: ").split()))

x = num.intersection(num2)
k = len(x)

print(k)

# Задание 3
num = input("Введите числа через пробел: ").split()
list1 = set()

for number in num:
    if number in list1:
        print("YES")
    else:
        print("NO")
        list1.add(number)