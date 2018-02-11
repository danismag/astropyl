from math import *

""""
    Проверяет корректность даты
    Выбрасывает необходимые исключения
    В случае успеха возвращает True
"""""


def correctdate(day, month, year):
    # Проверка аргументов
    if year != floor(year):
        raise ValueError("Год должен быть целым числом")
    if month not in range(1, 13):
        raise ValueError("Месяц должен быть в диапазоне 1-12")
    if month != floor(month):
        raise ValueError("Месяц не может быть дробным")
    if day < 0 or day >= 32:
        raise ValueError("Дата должна быть в диапазоне 0-31")
    return True
