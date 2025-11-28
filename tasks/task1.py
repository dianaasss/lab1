import time
from time_package.my_time import Time, make_Time

if __name__ == "__main__":
    print("Создание объекта через ввод с клавиатуры:")
    my_time = Time(1, 1)
    my_time.read()
    my_time.display()
    print("Всего минут:", my_time.minutes())