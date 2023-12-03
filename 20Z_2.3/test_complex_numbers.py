from complex_numbers import ComplexNumber
from pytest import approx, raises


def test_create_complex_number():
    complex_number = ComplexNumber(1, 8)
    assert complex_number.real_part == 1
    assert complex_number.imaginary_part == 8


def test_create_complex_number_floats():
    complex_number = ComplexNumber(1.4, -8.6)
    assert complex_number.real_part == 1.4
    assert complex_number.imaginary_part == -8.6


def test_complex_number_text():
    complex_number1 = ComplexNumber(1, 8)
    complex_number2 = ComplexNumber(1, -8)
    assert str(complex_number1) == "1 + 8i"
    assert str(complex_number2) == "1 - 8i"


def test_complex_number_text_floats():
    complex_number1 = ComplexNumber(1.4, 8.8)
    complex_number2 = ComplexNumber(1.4, -8.8)
    assert str(complex_number1) == "1.4 + 8.8i"
    assert str(complex_number2) == "1.4 - 8.8i"


def test_add_complex_numbers():
    complex_number1 = ComplexNumber(2, 5)
    complex_number2 = ComplexNumber(4, 7)
    new_complex_number = complex_number1 + complex_number2
    assert new_complex_number.real_part == 6
    assert new_complex_number.imaginary_part == 12


def test_subtract_complex_numbers():
    complex_number1 = ComplexNumber(2, 5)
    complex_number2 = ComplexNumber(4, 7)
    new_complex_number = complex_number1 - complex_number2
    assert new_complex_number.real_part == -2
    assert new_complex_number.imaginary_part == -2


def test_multiply_complex_numbers():
    complex_number1 = ComplexNumber(2, 5)
    complex_number2 = ComplexNumber(4, 7)
    new_complex_number = complex_number1 * complex_number2
    assert new_complex_number.real_part == -27
    assert new_complex_number.imaginary_part == 34


def test_divide_complex_numbers_int_result():
    complex_number1 = ComplexNumber(1, 8)
    complex_number2 = ComplexNumber(2, 3)
    new_complex_number = complex_number1 / complex_number2
    assert new_complex_number.real_part == 2
    assert new_complex_number.imaginary_part == 1


def test_divide_complex_numbers_float_result():
    complex_number1 = ComplexNumber(2, 5)
    complex_number2 = ComplexNumber(4, 7)
    new_complex_number = complex_number1 / complex_number2
    assert new_complex_number.real_part == approx(0.6615384615384615)
    assert new_complex_number.imaginary_part == approx(0.0923076923076923)


def test_divide_complex_numbers_imaginary_are_zeros():
    complex_number1 = ComplexNumber(1, 0)
    complex_number2 = ComplexNumber(2, 0)
    new_complex_number = complex_number1 / complex_number2
    assert new_complex_number.real_part == 0.5
    assert new_complex_number.imaginary_part == 0


def test_divide_complex_numbers_imaginary_by_zero():
    complex_number1 = ComplexNumber(1, 3)
    complex_number2 = ComplexNumber(0, 0)
    with raises(ZeroDivisionError):
        complex_number1 / complex_number2


def test_conjugate_complex_number():
    complex_number = ComplexNumber(1, 8)
    assert complex_number.real_part == 1
    assert complex_number.imaginary_part == 8
    conjugate = complex_number.conjugate()
    assert conjugate.real_part == 1
    assert conjugate.imaginary_part == -8


def test_conjugate_complex_number_imaginary_zero():
    complex_number = ComplexNumber(1, 0)
    assert complex_number.real_part == 1
    assert complex_number.imaginary_part == 0
    conjugate = complex_number.conjugate()
    assert conjugate.real_part == 1
    assert conjugate.imaginary_part == 0


def test_conjugate_complex_number_zeros():
    complex_number = ComplexNumber(0, 0)
    assert complex_number.real_part == 0
    assert complex_number.imaginary_part == 0
    conjugate = complex_number.conjugate()
    assert conjugate.real_part == 0
    assert conjugate.imaginary_part == 0


def test_int_modulus_complex_number():
    complex_number = ComplexNumber(4, 3)
    result = complex_number.modulus()
    assert result == 5


def test_modulus_complex_number_zeros():
    complex_number = ComplexNumber(0, 0)
    result = complex_number.modulus()
    assert result == 0


def test_float_modulus_complex_number():
    complex_number = ComplexNumber(1, 8)
    result = complex_number.modulus()
    assert result == 8.06225774829855
