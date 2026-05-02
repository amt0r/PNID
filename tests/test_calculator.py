"""Тести для модуля калькулятора."""

import pytest
from app.calculator import add, subtract, multiply, divide, power, sqrt, factorial


# ──────────────────────────────────────────────
# Тести додавання
# ──────────────────────────────────────────────
class TestAdd:
    """Тести функції add."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

    def test_add_zero(self):
        assert add(0, 0) == 0

    def test_add_float(self):
        assert add(1.5, 2.5) == 4.0


# ──────────────────────────────────────────────
# Тести віднімання
# ──────────────────────────────────────────────
class TestSubtract:
    """Тести функції subtract."""

    def test_subtract_positive(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative(self):
        assert subtract(-1, -1) == 0

    def test_subtract_zero(self):
        assert subtract(0, 0) == 0


# ──────────────────────────────────────────────
# Тести множення
# ──────────────────────────────────────────────
class TestMultiply:
    """Тести функції multiply."""

    def test_multiply_positive(self):
        assert multiply(2, 3) == 6

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6

    def test_multiply_zero(self):
        assert multiply(0, 100) == 0


# ──────────────────────────────────────────────
# Тести ділення
# ──────────────────────────────────────────────
class TestDivide:
    """Тести функції divide."""

    def test_divide_positive(self):
        assert divide(6, 3) == 2.0

    def test_divide_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Ділення на нуль"):
            divide(1, 0)


# ──────────────────────────────────────────────
# Тести піднесення до степеня
# ──────────────────────────────────────────────
class TestPower:
    """Тести функції power."""

    def test_power_positive(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -1) == 0.5


# ──────────────────────────────────────────────
# Тести квадратного кореня
# ──────────────────────────────────────────────
class TestSqrt:
    """Тести функції sqrt."""

    def test_sqrt_positive(self):
        assert sqrt(4) == 2.0

    def test_sqrt_zero(self):
        assert sqrt(0) == 0.0

    def test_sqrt_negative(self):
        with pytest.raises(ValueError, match="від'ємного"):
            sqrt(-1)


# ──────────────────────────────────────────────
# Тести факторіалу
# ──────────────────────────────────────────────
class TestFactorial:
    """Тести функції factorial."""

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_negative(self):
        with pytest.raises(ValueError, match="невід'ємних цілих"):
            factorial(-1)

    def test_factorial_float(self):
        with pytest.raises(ValueError):
            factorial(2.5)
