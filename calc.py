# Автор: Соколова Елена


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """
    Функция возвращает произведение
    param a: первое число
    param b: второе число
    return: вовзращает результат произведения
    """
    return a * b


import math

def sqrt(x):
    return math.sqrt(x)


if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")


