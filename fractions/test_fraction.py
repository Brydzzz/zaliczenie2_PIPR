from fraction import Fraction, ZeroDenominatorError
import pytest


def test_create_fraction_normalized():
    fraction = Fraction(1, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 4


def test_create_fraction_not_normalized():
    fraction = Fraction(2, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 2


def test_create_fraction_numerator_bigger_than_denominator():
    fraction = Fraction(15, 4)
    assert fraction.numerator == 15
    assert fraction.denominator == 4


def test_create_fraction_denominator_is_zero():
    with pytest.raises(ZeroDenominatorError):
        Fraction(1, 0)


def test_create_fraction_numerator_is_zero():
    fraction = Fraction(0, 3)
    assert fraction.numerator == 0
    assert fraction.denominator == 1


def test_create_fraction_negative_normalized():
    fraction = Fraction(-1, 3)
    assert fraction.numerator == -1
    assert fraction.denominator == 3


def test_create_fraction_one_negative_representation():
    fraction1 = Fraction(7, -3)
    fraction2 = Fraction(-7, 3)
    assert fraction1.numerator == fraction2.numerator == -7
    assert fraction1.denominator == fraction2.denominator == 3


def test_create_fraction_negative_not_normalized():
    fraction = Fraction(-2, 6)
    assert fraction.numerator == -1
    assert fraction.denominator == 3


def test_set_fraction_normalized():
    fraction = Fraction(1, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 4
    fraction.set_numerator_and_denominator(2, 7)
    assert fraction.numerator == 2
    assert fraction.denominator == 7


def test_set_fraction_not_normalized():
    fraction = Fraction(1, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 4
    fraction.set_numerator_and_denominator(2, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 2


def test_set_fraction_denominator_is_zero():
    fraction = Fraction(1, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 4
    with pytest.raises(ZeroDenominatorError):
        fraction.set_numerator_and_denominator(2, 0)


def test_add_typical():
    fraction1 = Fraction(1, 7)
    fraction2 = Fraction(3, 7)
    result = fraction1 + fraction2
    assert result.numerator == 4
    assert result.denominator == 7


def test_add_negative():
    fraction1 = Fraction(-1, 7)
    fraction2 = Fraction(-3, 7)
    result = fraction1 + fraction2
    assert result.numerator == -4
    assert result.denominator == 7


def test_add_different_denominators():
    fraction1 = Fraction(-1, 2)
    fraction2 = Fraction(1, 4)
    result = fraction1 + fraction2
    assert result.numerator == -1
    assert result.denominator == 4
