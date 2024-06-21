# Задание 1
pets = {}

pet_name = input("Введите имя питомца: ")
type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

if age % 10 == 1 and age % 100 != 11:
    age_str = str(age) + " год"
elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
    age_str = str(age) + " года"
else:
    age_str = str(age) + " лет"

pets[pet_name] = {
    "Вид питомца": type,
    "Возраст питомца": age_str,
    "Имя владельца": owner_name
}
print("Это " + type + " по кличке '" + pet_name + "'. Возраст питомца: " + age_str + ". Имя владельца: " + owner_name + ".")

# Задание 2
x = {}

for i in range(10, -6, -1):
    x[i] = i ** i

print(x)