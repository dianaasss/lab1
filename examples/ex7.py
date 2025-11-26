class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height

# Пример использования
rect = Rectangle(5, 3)

print("Ширина:", rect.get_width())    # 5
print("Высота:", rect.get_height())   # 3
print("Площадь:", rect.area())        # 15

# Изменяем размеры
rect.set_width(7)
rect.set_height(4)

print("\nПосле изменения:")
print("Ширина:", rect.get_width())    # 7
print("Высота:", rect.get_height())   # 4
print("Площадь:", rect.area())        # 28