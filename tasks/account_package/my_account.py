class Account:
    def __init__(self, owner='', account_number='', interest_rate=0.0, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = balance

    def read(self):
        self.owner = input("Введите фамилию владельца: ")
        self.account_number = input("Введите номер счета: ")
        self.interest_rate = float(input("Введите процент начисления: "))
        self.balance = float(input("Введите начальную сумму в рублях: "))

    def display(self):
        print(f"Владелец: {self.owner}")
        print(f"Номер счета: {self.account_number}")
        print(f"Процент: {self.interest_rate}%")
        print(f"Баланс: {self.balance:.2f} руб.")

    def change_owner(self, new_owner):
        self.owner = new_owner
        print(f"Владелец счета изменен на {self.owner}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств для снятия.")
        else:
            self.balance -= amount
            print(f"Снято {amount:.2f} руб. Текущий баланс: {self.balance:.2f} руб.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Внесено {amount:.2f} руб. Текущий баланс: {self.balance:.2f} руб.")

    def accrue_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)
        print(f"Начислены проценты: {self.interest_rate}%. Текущий баланс: {self.balance:.2f} руб.")

    def to_dollars(self, rate=80.0):
        dollars = self.balance / rate
        print(f"Баланс в долларах: {dollars:.2f} $")
        return dollars

    def to_euros(self, rate=90.0):
        euros = self.balance / rate
        print(f"Баланс в евро: {euros:.2f} €")
        return euros

    def amount_in_words(self):
        words = self.number_to_words(int(self.balance))
        print(f"Баланс прописью: {words} рублей")
        return words

    @staticmethod
    def number_to_words(n):
        units = ["","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
        tens = ["","десять","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"]
        teens = ["десять","одиннадцать","двенадцать","тринадцать","четырнадцать",
                 "пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
        hundreds = ["","сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот"]

        if n == 0:
            return "ноль"

        words = []

        if n >= 1000000:
            m = n // 1000000
            words.append(Account.number_to_words(m) + " миллион")
            n %= 1000000

        if n >= 1000:
            t = n // 1000
            if t == 1:
                words.append("одна тысяча")
            elif t == 2:
                words.append("две тысячи")
            else:
                words.append(Account.number_to_words(t) + " тысяч")
            n %= 1000

        if n >= 100:
            h = n // 100
            words.append(hundreds[h])
            n %= 100

        if 10 <= n <= 19:
            words.append(teens[n-10])
            n = 0

        if n >= 10:
            t = n // 10
            words.append(tens[t])
            n %= 10

        if n > 0:
            words.append(units[n])

        return ' '.join(words)

