class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("Width must be positive")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError("Height must be positive")

    def area(self):
        return self.__width * self.__height

# Пример использования
rect = Rectangle(5, 3)

print("Ширина:", rect.width)    # 5 (работает геттер)
print("Высота:", rect.height)   # 3 (работает геттер)
print("Площадь:", rect.area())  # 15

# Изменяем размеры через сеттеры
rect.width = 7    # работает сеттер
rect.height = 4   # работает сеттер

print("\nПосле изменения:")
print("Ширина:", rect.width)    # 7
print("Высота:", rect.height)   # 4
print("Площадь:", rect.area())  # 28

# Попытка установить отрицательное значение
try:
    rect.width = -5  # вызовет ValueError
except ValueError as e:
    print("Ошибка:", e)