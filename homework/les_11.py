# Задание 1
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
def list1(n):
    result = []
    for i in range(n, 0, -1):
        result.append(factorial(i))
    return result

n = int(input("Введите целое число: "))
fact_n = factorial(n)
result_list = list1(fact_n)
print("Список факториалов:", result_list)

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

    pet_name = input("Введите кличку питомца: ")
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
    print(f"Питомец {pet_name} добавлен с ID {new_id}.")

def read(ID):
    pet = get_pet(ID)
    if pet:
        for pet_name, pet_info in pet.items():
            print(f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_info['Возраст питомца']} {get_suffix(pet_info['Возраст питомца'])}. Имя владельца: {pet_info['Имя владельца']}.")
    else:
        print(f"Питомец с ID {ID} не найден.")

def update(ID):
    pet = get_pet(ID)
    if pet:
        for pet_name, pet_info in pet.items():
            print(f"Текущая информация о питомце {pet_name}:")
            print(f"Вид питомца: {pet_info['Вид питомца']}")
            print(f"Возраст питомца: {pet_info['Возраст питомца']}")
            print(f"Имя владельца: {pet_info['Имя владельца']}")

        update_field = input("Какое поле хотите обновить? (Вид питомца, Возраст питомца, Имя владельца): ")
        new_value = input("Введите новое значение: ")

        pet_info[update_field] = new_value
        print(f"Информация о питомце {pet_name} обновлена.")
    else:
        print(f"Питомец с ID {ID} не найден.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f"Запись о питомце с ID {ID} удалена.")
    else:
        print(f"Питомец с ID {ID} не найден.")

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and not 12 <= age % 100 <= 14:
        return 'года'
    else:
        return 'лет'

def pets_list():
    if pets:
        for ID, pet in pets.items():
            for pet_name, pet_info in pet.items():
                print(f"ID: {ID}")
                print(f"Кличка: {pet_name}")
                print(f"Вид: {pet_info['Вид питомца']}")
                print(f"Возраст: {pet_info['Возраст питомца']}")
                print(f"Владелец: {pet_info['Имя владельца']}")
                print("-" * 20)  
    else:
        print("В базе данных нет питомцев.")

while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ").lower()

    if command == 'create':
        create()
    elif command == 'read':
        ID = int(input("Введите ID питомца: "))
        read(ID)
    elif command == 'update':
        ID = int(input("Введите ID питомца: "))
        update(ID)
    elif command == 'delete':
        ID = int(input("Введите ID питомца: "))
        delete(ID)
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        break
    else:
        print("Неверная команда.")