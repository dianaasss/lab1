class Time:
    def __init__(self, hours, mins):
        if not isinstance(hours, int) or hours <= 0:
            print("Ошибка: часы должны быть целым положительным числом")
            exit(1)
        if not isinstance(mins, int) or mins <= 0:
            print("Ошибка: минуты должны быть целым положительным числом")
            exit(1)
        self.hours = hours
        self.mins = mins

    def read(self):
        try:
            h = int(input("Введите часы (целое положительное число): "))
            m = int(input("Введите минуты (целое положительное число): "))
            if h <= 0 or m <= 0:
                print("Ошибка: введены не положительные числа")
                exit(1)
            self.hours = h
            self.mins = m
        except ValueError:
            print("Ошибка: введены некорректные данные")
            exit(1)

    def display(self):
        print(f"Время: {self.hours} часов {self.mins} минут")

    def minutes(self):
        return self.hours * 60 + self.mins


def make_Time(hh, mm):
    return Time(hh, mm)