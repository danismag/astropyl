from math import *

""""Перевод даты в юлианские дни"""


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
        A = year // 100
        B = 2 - A + A // 4
    else:
        B = 0
    C = floor(365.25*year)
    D = floor(30.6001*(month + 1))

    return B + C +D + day + 1720994.5


assert juliandate(1985, 2, 17.25), "функция существует"
assert juliandate(1985, 2, 17.25) == 2446113.75

