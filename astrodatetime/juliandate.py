from math import *

""""Перевод даты в юлианские дни
    Начало отсчета дней от точки январь 0.0
    что обозначает полночь 30-31 декабря
"""


def juliandate(year, month, day):
    # Проверка корректности аргументов
    if year != floor(year):
        raise ValueError("Год должен быть целым числом")
    if month not in range(1, 13):
        raise ValueError("Месяц должен быть в диапазоне 1-12")
    if month != floor(month):
        raise ValueError("Месяц не может быть дробным")
    if day < 0 or day >= 32:
        raise ValueError("Дата должна быть в диапазоне 0-31")

    # Проверека на григорианское летоисчисление
    if (year + month/12 + day/365) >= 1582 + 10/12 + 15/365:
        gregorian = True
    else:
        gregorian = False

    # Поправка для годов до нашей эры (нет нулевого года)
    if year < 0:
        year += 1

    if month <= 2:
        year -= 1
        month += 12

    if gregorian:
        a = year // 100
        b = 2 - a + (a // 4)
    else:
        b = 0
    c = floor(365.25*year)
    d = floor(30.6001*(month + 1))

    return b + c + d + day + 1720994.5
