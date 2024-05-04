#Задача 1
str = input("Введите буквы без пробелов: ")
def is_palindrome(s):
    return s == s[::-1]

if is_palindrome(str):
    print("yes")
else:
    print("no")
    
#Задача 2
str = input("Введите различные символы с пробелами: ")
def dell(s):
    return ' '.join(s.split())

print(dell(str))