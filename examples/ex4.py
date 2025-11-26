class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print('{} has sailed!'.format(self.name))

    def sail_function(name):
        print('{} has sailed!'.format(name))

    def convert_cargo(self):
        cargo_kg = self.cargo * 1000
        return cargo_kg

# Создаём корабль
black_pearl = Ship('Black Pearl', 800)

# Используем методы
black_pearl.sail()  # Black Pearl has sailed!
Ship.sail_function(black_pearl.name)  # Black Pearl has sailed!

# Устанавливаем груз и конвертируем
black_pearl.cargo = 50  # добавляем груз
print(black_pearl.convert_cargo())  # 50000