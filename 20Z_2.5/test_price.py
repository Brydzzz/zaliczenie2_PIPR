from price import Price, UnavailableCurrency, NegativePriceError
from pytest import raises


def test_create_price():
    price = Price("PLN", 120)
    assert price.currency == "PLN"
    assert price.value == 120


def test_create_price_wrong_currency():
    with raises(UnavailableCurrency):
        Price("PN", 120)


def test_invalid_price():
    with raises(NegativePriceError):
        Price("PLN", -10)


def test_add_price_same_currency():
    price_1 = Price("PLN", 120)
    price_2 = Price("PLN", 120)
    result = price_1.add_price(price_2)
    assert result.currency == "PLN"
    assert result.value == 240


def test_add_price_different_currency():
    price_1 = Price("PLN", 120)
    price_2 = Price("EUR", 120)
    result = price_1.add_price(price_2)
    assert result.currency == "PLN"
    assert result.value == 600


def test_add_price_given_currency():
    price_1 = Price("PLN", 120)
    price_2 = Price("PLN", 120)
    result = price_1.add_price(price_2, "EUR")
    assert result.currency == "EUR"
    assert result.value == 60


def test_add_price_result_with_decimal_point():
    price_1 = Price("PLN", 120)
    price_2 = Price("USD", 120)
    result = price_1.add_price(price_2, "EUR")
    assert result.currency == "EUR"
    assert result.value == 140


def test_subtract_price_same_currency():
    price_1 = Price("PLN", 120)
    price_2 = Price("PLN", 120)
    result = price_1.subtract_price(price_2)
    assert result.currency == "PLN"
    assert result.value == 0


def test_subtract_price_different_currency():
    price_1 = Price("PLN", 120)
    price_2 = Price("EUR", 20)
    result = price_1.subtract_price(price_2)
    assert result.currency == "PLN"
    assert result.value == 40


def test_subtract_price_given_currency():
    price_1 = Price("PLN", 120)
    price_2 = Price("PLN", 120)
    result = price_1.subtract_price(price_2, "EUR")
    assert result.currency == "EUR"
    assert result.value == 0


def test_subtract_price_result_with_decimal_point():
    price_1 = Price("PLN", 120)
    price_2 = Price("USD", 20)
    result = price_1.subtract_price(price_2, "EUR")
    assert result.currency == "EUR"
    assert result.value == 12


def test_subtract_price_result_negative():
    price_1 = Price("PLN", 120)
    price_2 = Price("USD", 120)
    with raises(NegativePriceError):
        price_1.subtract_price(price_2, "EUR")


def test_multiply_by_const_int():
    price = Price("PLN", 120)
    result = price.multiply_by_const(3)
    assert result.currency == "PLN"
    assert result.value == 360


def test_multiply_by_const_float():
    price = Price("PLN", 120)
    result = price.multiply_by_const(3.61)
    assert result.currency == "PLN"
    assert result.value == 433


def test_price_text_typical():
    price = Price("PLN", 120)
    assert str(price) == "1.20 PLN"


def test_price_text_one_small_unit():
    price = Price("PLN", 102)
    assert str(price) == "1.02 PLN"


def test_price_text_zero():
    price = Price("PLN", 0)
    assert str(price) == "0.00 PLN"


def test_price_text_big():
    price = Price("PLN", 12000013)
    assert str(price) == "120000.13 PLN"
