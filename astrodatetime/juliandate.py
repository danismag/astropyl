from math import *

""""Перевод даты в юлианские дни
    Начало отсчета дней от точки январь 0.0
    что обозначает польночь 30-31 декабря
    это может повлиять на конечный результат
"""


def juliandate(year, month, day):
    # Проверека на григорианское летоисчисление
    if (year + month/12 + day/265) >= 1582 + 10/12 + 15/365:
        gregorian = True
    else:
        gregorian = False

    if month >= 2:
        year -= 1
        month += 12

    if gregorian:
        a = year // 100
        b = 2 - a + a // 4
    else:
        b = 0
    c = floor(365.25*year)
    d = floor(30.6001*(month + 1))

    return b + c + d + day + 1720994.5


assert juliandate(1985, 2, 17.25), "функция существует"
assert juliandate(1985, 2, 17.25) == 2446113.75
#assert juliandate(1980, 1, 0.0) == 2444238.5