class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def name_captain(self, cap):
        self.captain = cap
        print('{} is the captain of the {}'.format(self.captain, self.name))

black_pearl = Ship('Black Pearl', 800)
black_pearl.name_captain('Jack Sparrow')
print(black_pearl.captain)