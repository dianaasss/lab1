from account_package.my_account import Account

if __name__ == "__main__":
    account1 = Account()
    print("Создание первого счета:")
    account1.read()

    # Сначала снимаем сумму
    withdraw_amount = float(input("Введите сумму для снятия: "))
    account1.withdraw(withdraw_amount)

    # Потом вносим сумму
    deposit_amount = float(input("Введите сумму для внесения: "))
    account1.deposit(deposit_amount)

    # Начисляем проценты
    account1.accrue_interest()

    # Итоговый баланс
    print("\nИтоговый баланс первого счета:")
    account1.display()
    account1.to_dollars()
    account1.to_euros()
    account1.amount_in_words()

    # Замена владельца и повтор операций
    print("\nЗамена владельца и повтор операций:")
    new_owner = input("Введите нового владельца счета: ")
    account1.change_owner(new_owner)

    withdraw_amount = float(input("Введите сумму для снятия: "))
    account1.withdraw(withdraw_amount)

    deposit_amount = float(input("Введите сумму для внесения: "))
    account1.deposit(deposit_amount)

    account1.accrue_interest()

    print("\nИтоговый баланс после смены владельца:")
    account1.display()
    account1.to_dollars()
    account1.to_euros()
    account1.amount_in_words()