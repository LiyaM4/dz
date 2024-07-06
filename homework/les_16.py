# Задание 1
class kassa:
    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        self.balance += X
        print(f"Баланс пополнен на {X} единиц. Текущий баланс: {self.balance}")

    def count_1000(self):
        thousands = self.balance // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands

    def take_away(self, X):
        if X <= self.balance:
            self.balance -= X
            print(f"Снято {X} единиц. Текущий баланс: {self.balance}")
        else:
            print(f"Недостаточно средств для снятия {X} единиц. Текущий баланс: {self.balance}")
kassa = kassa()
kassa.top_up(4000)
kassa.count_1000()
kassa.take_away(1000)
kassa.count_1000()

try:
    kassa.take_away(6000)
except ValueError as e:
    print(e)
# Задание 2
class Черепашка:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Черепашка не может двигаться на 0 клеток.")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return max(dx // self.s, dy // self.s) 

cherepashka = Черепашка(0, 0, 2)
print(f"Текущая позиция: ({cherepashka.x}, {cherepashka.y})")
print(f"Скорость: {cherepashka.s}")

cherepashka.go_right()
cherepashka.go_up()
print(f"Новая позиция: ({cherepashka.x}, {cherepashka.y})")

cherepashka.evolve()
print(f"Скорость: {cherepashka.s}")

cherepashka.degrade()
print(f"Скорость: {cherepashka.s}")

try:
    cherepashka.degrade()
except ValueError as e:
    print(e)

print(f"Минимальное кол-во действий до (9, 5): {cherepashka.count_moves(9, 5)}")