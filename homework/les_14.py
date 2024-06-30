my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rec(index):
  if index < len(my_list):
    print(my_list[index])
    rec(index + 1)  
  else:
    print("Конец списка")

rec(0) 