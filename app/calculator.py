"""Модуль калькулятора — демонстраційний додаток для CI/CD."""

import math


def add(a: float, b: float) -> float:
    """Повертає суму двох чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Повертає різницю двох чисел."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Повертає добуток двох чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Повертає частку двох чисел.

    Raises:
        ValueError: Якщо дільник дорівнює нулю.
    """
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


def power(base: float, exponent: float) -> float:
    """Повертає результат піднесення до степеня."""
    return base ** exponent


def sqrt(a: float) -> float:
    """Повертає квадратний корінь числа.

    Raises:
        ValueError: Якщо число від'ємне.
    """
    if a < 0:
        raise ValueError("Квадратний корінь від'ємного числа не визначений")
    return math.sqrt(a)


def factorial(n: int) -> int:
    """Повертає факторіал числа.

    Raises:
        ValueError: Якщо число від'ємне або не ціле.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних цілих чисел")
    return math.factorial(n)
