
import pytest
from my_time import Time, make_Time


def test_creation_valid():
    time = Time(2, 30)
    assert time.hours == 2
    assert time.mins == 30
    assert time.minutes() == 150


def test_creation_invalid_hours():
    with pytest.raises(SystemExit):
        Time(-1, 30)


def test_creation_invalid_minutes():
    with pytest.raises(SystemExit):
        Time(2, -5)


def test_creation_zero_values():
    with pytest.raises(SystemExit):
        Time(0, 30)
    with pytest.raises(SystemExit):
        Time(2, 0)


def test_minutes_calculation():
    test_cases = [
        (1, 30, 90),
        (2, 0, 120),
        (0, 45, 45),
        (3, 15, 195)
    ]
    
    for hours, mins, expected_minutes in test_cases:
        if hours > 0 and mins > 0:
            time = Time(hours, mins)
            assert time.minutes() == expected_minutes


def test_display(capsys):
    time = Time(3, 45)
    time.display()
    
    captured = capsys.readouterr()
    assert "Время: 3 часов 45 минут" in captured.out


def test_read_valid_input(monkeypatch):
    time = Time(1, 1)  # создаем с временными значениями
    
    inputs = iter(["5", "20"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    time.read()
    
    assert time.hours == 5
    assert time.mins == 20
    assert time.minutes() == 320


def test_read_invalid_negative(monkeypatch):
    time = Time(1, 1)
    
    inputs = iter(["-5", "20"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        time.read()


def test_read_invalid_zero(monkeypatch):
    time = Time(1, 1)
    
    inputs = iter(["0", "30"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        time.read()


def test_read_invalid_type(monkeypatch):
    time = Time(1, 1)
    
    inputs = iter(["abc", "30"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        time.read()


def test_make_Time_function():
    time = make_Time(4, 15)
    
    assert isinstance(time, Time)
    assert time.hours == 4
    assert time.mins == 15
    assert time.minutes() == 255


def test_make_Time_invalid():
    with pytest.raises(SystemExit):
        make_Time(-1, 30)


def test_edge_cases():

    time1 = Time(1, 1)
    assert time1.minutes() == 61
    

    time2 = Time(24, 59)
    assert time2.minutes() == 24 * 60 + 59


def test_consistency():
    time = Time(2, 45)
    
    expected_minutes = time.hours * 60 + time.mins
    assert time.minutes() == expected_minutes
    
def test_string_representation():
    time = Time(2, 30)


if __name__ == "__main__":

    pytest.main([__file__, "-v"])