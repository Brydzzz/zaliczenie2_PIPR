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


def test_add_bigger_than_one_fractions():
    fraction1 = Fraction(-10, 2)
    fraction2 = Fraction(13, 4)
    result = fraction1 + fraction2
    assert result.numerator == -7
    assert result.denominator == 4


def test_sub_typical():
    fraction1 = Fraction(1, 7)
    fraction2 = Fraction(3, 7)
    result = fraction1 - fraction2
    assert result.numerator == -2
    assert result.denominator == 7


def test_sub_negative():
    fraction1 = Fraction(-1, 7)
    fraction2 = Fraction(-3, 7)
    result = fraction1 - fraction2
    assert result.numerator == 2
    assert result.denominator == 7


def test_sub_different_denominators():
    fraction1 = Fraction(-1, 2)
    fraction2 = Fraction(1, 4)
    result = fraction1 - fraction2
    assert result.numerator == -3
    assert result.denominator == 4


def test_sub_bigger_than_one_fractions():
    fraction1 = Fraction(-10, 2)
    fraction2 = Fraction(13, 4)
    result = fraction1 - fraction2
    assert result.numerator == -33
    assert result.denominator == 4


def test_multiply_typical():
    fraction1 = Fraction(1, 7)
    fraction2 = Fraction(3, 7)
    result = fraction1 * fraction2
    assert result.numerator == 3
    assert result.denominator == 49


def test_multiply_negative():
    fraction1 = Fraction(-1, 7)
    fraction2 = Fraction(-3, 7)
    result = fraction1 * fraction2
    assert result.numerator == 3
    assert result.denominator == 49


def test_multiply_different_denominators():
    fraction1 = Fraction(-1, 2)
    fraction2 = Fraction(1, 4)
    result = fraction1 * fraction2
    assert result.numerator == -1
    assert result.denominator == 8


def test_multiply_bigger_than_one_fractions():
    fraction1 = Fraction(-10, 2)
    fraction2 = Fraction(13, 4)
    result = fraction1 * fraction2
    assert result.numerator == -65
    assert result.denominator == 4


def test_divide_typical():
    fraction1 = Fraction(1, 7)
    fraction2 = Fraction(3, 7)
    result = fraction1 / fraction2
    assert result.numerator == 1
    assert result.denominator == 3


def test_divide_negative():
    fraction1 = Fraction(-1, 7)
    fraction2 = Fraction(-3, 7)
    result = fraction1 / fraction2
    assert result.numerator == 1
    assert result.denominator == 3


def test_divide_different_denominators():
    fraction1 = Fraction(-1, 2)
    fraction2 = Fraction(1, 4)
    result = fraction1 / fraction2
    assert result.numerator == -2
    assert result.denominator == 1


def test_divide_bigger_than_one_fractions():
    fraction1 = Fraction(-10, 2)
    fraction2 = Fraction(13, 4)
    result = fraction1 / fraction2
    assert result.numerator == -20
    assert result.denominator == 13


def test_divide_by_zero():
    fraction1 = Fraction(-1, 2)
    fraction2 = Fraction(0, 4)
    with pytest.raises(ZeroDivisionError):
        fraction1 / fraction2


def test_add_integer_typical():
    fraction = Fraction(1, 7)
    result = fraction.add_integer(3)
    assert result.numerator == 22
    assert result.denominator == 7


def test_add_integer_negative():
    fraction = Fraction(-1, 7)
    result = fraction.add_integer(3)
    assert result.numerator == 20
    assert result.denominator == 7


def test_add_integer_fraction_bigger_than_one():
    fraction = Fraction(11, 2)
    result = fraction.add_integer(1)
    assert result.numerator == 13
    assert result.denominator == 2


def test_give_real_value_positive():
    fraction = Fraction(11, 2)
    result = fraction.give_real_value()
    assert result == 5.5


def test_give_real_value_negative():
    fraction = Fraction(-11, 2)
    result = fraction.give_real_value()
    assert result == -5.5


def test_give_real_zero():
    fraction = Fraction(0, 2)
    result = fraction.give_real_value()
    assert result == 0


def test_give_real_irrational():
    fraction = Fraction(1, 3)
    result = fraction.give_real_value()
    assert result == pytest.approx(0.3333333)


def test_fraction_as_str_typical():
    fraction = Fraction(1, 3)
    assert str(fraction) == "1/3"


def test_fraction_as_str_negative():
    fraction = Fraction(1, -3)
    assert str(fraction) == "-1/3"


def test_fraction_as_str_zero():
    fraction = Fraction(0, -3)
    assert str(fraction) == "0/1"
