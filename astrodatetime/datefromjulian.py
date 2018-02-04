from math import *

""""
    Перевод юлианской даты в календарную
    Введена поправка для годов до н.э.
    Точка январь 0.0 соответствует полуночи 30-31 декабря
"""


def datefromjulian(jdate):
    result = {}
    # Проверка корректности аргументов
    if not isinstance(jdate, (int, float)):
        raise TypeError("Аргумент должен быть числовым (Юлианская дата)")
    if jdate < 0:
        raise ValueError("Юлинаская дата может быть только положительной")

    # Поправка для годов до н.э.
    if jdate < 1721423.5:   # Р.Х. - 1 янв 1 года н.э.
        yearshift = -1
    else:
        yearshift = 0

    jdate += 0.5
    i = floor(jdate)
    f = jdate - i
    if i > 2299160:
        a = (i - 1867216.25) // 36524.25
        b = i + 1 + a - (a // 4)
    else:
        b = i
    c = b + 1524
    d = (c - 122.1) // 365.25
    e1 = floor(365.25*d)
    g = (c - e1) // 30.6001
    result['day'] = c - e1 + f - floor(30.6001*g)

    if g < 13.5:
        m = g - 1
    else:
        m = g - 13
    result['month'] = m

    if m > 2.5:
        y = d - 4716
    else:
        y = d - 4715
    result['year'] = y + yearshift

    return result
