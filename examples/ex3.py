class Pet:
    kind = 'mammal'
    n_pets = 0 # количество питомцев
    pet_names = [] # список имен всех питомцев

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

tom = Pet('cat', 'Tom')
avocado = Pet('dog', 'Avocado')
ben = Pet('goldfish', 'Benjamin')

# получим доступ к атрибуту класса напрямую через класс
Pet.n_pets += 3
print(Pet.n_pets)
print(tom.n_pets)
print(avocado.n_pets)
print(ben.n_pets)

ben.kind = 'fish'
print(Pet.kind)
print(tom.kind)
print(avocado.kind)
print(ben.kind)

tom.pet_names.append(tom.name)
avocado.pet_names.append(avocado.name)
ben.pet_names.append(ben.name)
print(Pet.pet_names)
print(tom.pet_names)
print(avocado.pet_names)
print(ben.pet_names)

tom.pet_names = ['Tom']
avocado.pet_names = ['Avocado']
ben.pet_names = ['Benjamin']
print(Pet.pet_names)
print(tom.pet_names)
print(avocado.pet_names)
print(ben.pet_names)
# изменение атрибута экземпляра
ben.legs = 0

Pet.all_specs = [tom.spec, avocado.spec, ben.spec]
print(tom.all_specs)
print(avocado.all_specs)
print(ben.all_specs)

avocado.breed = 'corgi'