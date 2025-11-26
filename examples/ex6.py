class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
    
    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print('Loaded {} tons'.format(weight))
        else:
            print('Cannot load that much')
    
    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print('Unloaded {} tons'.format(weight))
        else:
            print('Cannot unload that much')
    
    # ДОБАВЬТЕ ЭТОТ МЕТОД В КЛАСС!
    def get_info(self):
        print("Ship: {}, Capacity: {} tons, Current cargo: {} tons".format(
            self.name, self.capacity, self.cargo))

# Только ПОСЛЕ этого создавайте объекты
ship1 = Ship("Titanic", 50000)
ship1.load_cargo(20000)
ship1.load_cargo(15000)
ship1.get_info()  # Теперь этот метод существует!
ship1.unload_cargo(10000)
ship1.get_info()