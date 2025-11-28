
import pytest
from io import StringIO
import sys
from my_account import Account


def test_account_creation_default():
    account = Account()
    assert account.owner == ''
    assert account.account_number == ''
    assert account.interest_rate == 0.0
    assert account.balance == 0.0


def test_account_creation_with_params():
    account = Account("Иванов", "1234567890", 5.0, 10000.0)
    assert account.owner == "Иванов"
    assert account.account_number == "1234567890"
    assert account.interest_rate == 5.0
    assert account.balance == 10000.0


def test_display(capsys):
    account = Account("Петров", "0987654321", 3.5, 5000.0)
    account.display()
    
    captured = capsys.readouterr()
    output = captured.out
    
    assert "Владелец: Петров" in output
    assert "Номер счета: 0987654321" in output
    assert "Процент: 3.5%" in output
    assert "Баланс: 5000.00 руб." in output


def test_change_owner():
    account = Account("Иванов", "123", 5.0, 1000.0)
    account.change_owner("Сидоров")
    
    assert account.owner == "Сидоров"


def test_deposit():
    account = Account(balance=1000.0)
    account.deposit(500.0)
    
    assert account.balance == 1500.0


def test_withdraw_success():
    account = Account(balance=1000.0)
    account.withdraw(300.0)
    
    assert account.balance == 700.0


def test_withdraw_insufficient_funds(capsys):
    account = Account(balance=100.0)
    account.withdraw(200.0)
    
    assert account.balance == 100.0
    
    captured = capsys.readouterr()
    assert "Недостаточно средств" in captured.out


def test_accrue_interest():
    account = Account(balance=1000.0, interest_rate=10.0)
    account.accrue_interest()
    
    assert account.balance == 1100.0  # 1000 + 10%


def test_to_dollars(capsys):
    account = Account(balance=8000.0)
    dollars = account.to_dollars(80.0)
    
    assert dollars == 100.0  # 8000 / 80 = 100
    
    captured = capsys.readouterr()
    assert "Баланс в долларах:" in captured.out


def test_to_euros(capsys):
    account = Account(balance=9000.0)
    euros = account.to_euros(90.0)
    
    assert euros == 100.0  # 9000 / 90 = 100
    
    captured = capsys.readouterr()
    assert "Баланс в евро:" in captured.out


def test_number_to_words_static():
    assert Account.number_to_words(0) == "ноль"
    assert Account.number_to_words(1) == "один"
    assert Account.number_to_words(10) == "десять"
    assert Account.number_to_words(15) == "пятнадцать"
    assert Account.number_to_words(25) == "двадцать пять"
    assert Account.number_to_words(100) == "сто"
    assert Account.number_to_words(123) == "сто двадцать три"
    assert Account.number_to_words(1000) == "одна тысяча"
    assert Account.number_to_words(2000) == "две тысячи"
    assert Account.number_to_words(3500) == "три тысячи пятьсот"


def test_amount_in_words(capsys):
    """Тест вывода суммы прописью"""
    account = Account(balance=1234.56)
    words = account.amount_in_words()

    assert "тысяча" in words
    assert "двести" in words
    assert "тридцать" in words
    assert "четыре" in words
    
    captured = capsys.readouterr()
    assert "Баланс прописью:" in captured.out
    assert "рублей" in captured.out


def test_complex_operations():
    """Тест комплексных операций"""
    account = Account("Тестов", "111", 5.0, 2000.0)
    

    account.deposit(1000.0)
    assert account.balance == 3000.0

    account.withdraw(500.0)
    assert account.balance == 2500.0

    account.accrue_interest()
    assert account.balance == 2625.0 
    
    account.change_owner("НовыйВладелец")
    assert account.owner == "НовыйВладелец"


def test_edge_cases():
    """Тест граничных случаев"""
    account = Account(balance=0.0)
    account.withdraw(100.0)
    assert account.balance == 0.0
    
    account = Account(balance=1000.0, interest_rate=-2.0)
    account.accrue_interest()
    assert account.balance == 980.0 


def test_negative_deposit():
    """Тест внесения отрицательной суммы"""
    account = Account(balance=1000.0)
    account.deposit(-100.0)

if __name__ == "__main__":

    pytest.main([__file__, "-v"])