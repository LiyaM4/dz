# # Задание 1
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n+1):
#         result *= i
#     return result
# def list1(n):
#     fact_n = factorial(n)
#     fact_list = [factorial(i) for i in range(n, 0, -1)]
#     return fact_n, fact_list

# n = int(input("Введите целое число: "))
# fact_n, result_list = list1(n)
# print("Список факториалов:", result_list)

# Задание 2
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"Питомец {pet_name} успешно добавлен в базу данных.")

def read(ID):
    if ID in pets:
        pet_data = pets[ID]
        pet_name = list(pet_data.keys())[0]
        pet_info = pet_data[pet_name]
        print(f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\".")
        print(f"Возраст питомца: {pet_info['Возраст питомца']} лет.")
        print(f"Имя владельца: {pet_info['Имя владельца']}")
    else:
        print(f"Питомца с ID {ID} не существует.")

def update(ID):
    if ID in pets:
        pet_data = pets[ID]
        pet_name = list(pet_data.keys())[0]
        print(f"Текущая информация о питомце {pet_name}:")
        print(f"Вид питомца: {pet_data[pet_name]['Вид питомца']}")
        print(f"Возраст питомца: {pet_data[pet_name]['Возраст питомца']}")
        print(f"Имя владельца: {pet_data[pet_name]['Имя владельца']}")
        print("Введите новые данные (или оставьте пустым, чтобы пропустить):")
        new_type = input("Новый вид питомца: ")
        new_age = input("Новый возраст питомца: ")
        new_owner = input("Новое имя владельца: ")
        if new_type:
            pet_data[pet_name]["Вид питомца"] = new_type
        if new_age:
            pet_data[pet_name]["Возраст питомца"] = int(new_age)
        if new_owner:
            pet_data[pet_name]["Имя владельца"] = new_owner
        print(f"Информация о питомце {pet_name} обновлена.")
    else:
        print(f"Питомца с ID {ID} не существует.")

def delete(ID):
    if ID in pets:
        pet_name = list(pets[ID].keys())[0]
        del pets[ID]
        print(f"Запись о питомце {pet_name} удалена.")
    else:
        print(f"Питомца с ID {ID} не существует.")

command = ""

while command != "stop":
    command = input("Введите команду (create, read, update, delete, stop): ")
    if command == "create":
        create()
    elif command == "read":
        ID = int(input("Введите ID питомца: "))
        read(ID)
    elif command == "update":
        ID = int(input("Введите ID питомца: "))
        update(ID)
    elif command == "delete":
        ID = int(input("Введите ID питомца: "))
        delete(ID)
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неверная команда.")