# Задание 1
a, b = map(float, input("Введите две стороны прямоугольника через пробел: ").split())
pr = 2*(a + b)
pd = a * b
print("Периметр: " + str(pr) + ". Площадь: " + str(pd))

# Задание 2
num = 12345
a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = (num // 1000) % 10
e = (num // 10000) % 10
print((b**a) * c / (e - d))
