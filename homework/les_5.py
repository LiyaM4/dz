# Задача 1
num = int(input("Введите целое число: "))
if num > 0:
    if num % 2 == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
elif num == 0:
    print("Нулевое число")
else:
    if num % 2 == 0:
        print("Отрицательное четное число")
    else:
        print("Отрицательное нечетное число")

# Задание 2
word = input("Введите слово: ")

v = "aeiou"
c = 0
v_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letter in word:
    if letter in v:
        v_counts[letter] += 1
    else:
        c += 1

print("Количество согласных букв:", c)
print("Количество гласных букв:", sum(v_counts.values()))

for v, count in v_counts.items():
    if count == 0:
        print(f"Буква '{v}': False")
    else:
        print(f"Буква '{v}': {count}")

# Задача 3
m = int(input("Сумма стартапа: "))
M = int(input("У Майкла: "))
I = int(input("У Ивана: "))
if M >= m and I >= m:
    print(2)
elif M >= m and I <= m:
    print("Mike")
elif M <= m and I >= m:
    print("Ivan")
elif (M <= m and I <= m) and (M + I > m):
    print(1)
else:
    print(0)