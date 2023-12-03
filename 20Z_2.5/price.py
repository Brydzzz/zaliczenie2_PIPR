class UnavailableCurrency(Exception):
    def __init__(self):
        super().__init__("Choosen currency is not available")


class NegativePriceError(Exception):
    def __init__(self):
        super().__init__("Price cannot be negative")


class Price:
    """
    currency possible values: PLN, USD, EUR
    """

    def __init__(self, currency: str, value: int):
        available_currencies = ["PLN", "USD", "EUR"]

        if currency not in available_currencies:
            raise UnavailableCurrency

        self._currency = currency

        if value < 0:
            raise NegativePriceError

        self._value = value

        self._converters = {
            "PLNPLN": 1,
            "EUREUR": 1,
            "USDUSD": 1,
            "PLNUSD": 0.25,
            "USDPLN": 4.2,
            "PLNEUR": 0.25,
            "EURPLN": 4,
            "USDEUR": 0.92,
            "EURUSD": 1.09,
        }

    @property
    def currency(self):
        return self._currency

    @property
    def value(self):
        return self._value

    @property
    def converters(self):
        return self._converters

    def add_price(self, other_price, currency: str = ""):
        """
        Adds price to price
        If currency was not given, sum's currency is first price's currency
        If currency was given converts prices and then adds them
        """
        if not currency:
            currency = self.currency
            if self.currency == other_price.currency:
                sum_value = self.value + other_price.value
            else:
                other_price.convert_price(currency)
                sum_value = self.value + other_price.value
        else:
            self.convert_price(currency)
            other_price.convert_price(currency)
            sum_value = self.value + other_price.value

        return Price(currency, sum_value)

    def subtract_price(self, other_price, currency: str = ""):
        """
        Subtract price from price
        If currency was not given, subtraction's currency is
        first price's currency
        If currency was given converts prices and then subtracts them
        """
        if not currency:
            currency = self.currency
            if self.currency == other_price.currency:
                subtract_value = self.value - other_price.value
            else:
                other_price.convert_price(currency)
                subtract_value = self.value - other_price.value
        else:
            self.convert_price(currency)
            other_price.convert_price(currency)
            subtract_value = self.value - other_price.value

        return Price(currency, subtract_value)

    def multiply_by_const(self, constant):
        """
        Mulitiplies price by constant
        """
        new_value = (self.value * constant) // 1
        return Price(self.currency, new_value)

    def convert_price(self, currency):
        converter = self.converters.get(self.currency + currency)
        self._value = (self.value * converter) // 1

    def __str__(self):
        main_unit = self.value // 100
        small_unit = self.value % 100
        return f"{main_unit}.{small_unit:02} {self.currency}"
