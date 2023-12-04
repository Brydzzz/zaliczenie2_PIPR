class ZeroDenominatorError(Exception):
    def __init__(self):
        super().__init__("Denominator cannot be zero")


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDenominatorError
        self._numerator = numerator
        self._denominator = denominator
        self.normalize()

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def find_gcd(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            modulo = a % b
            a = b
            b = modulo
        return a

    def normalize(self):
        gcd = self.find_gcd()
        if gcd != 1:
            normalized_numerator = self.numerator / gcd
            normalized_denominator = self.denominator / gcd
            self._numerator = int(normalized_numerator)
            self._denominator = int(normalized_denominator)

    def set_numerator_and_denominator(
        self, new_numerator: int, new_denominator: int
    ):
        if new_denominator == 0:
            raise ZeroDenominatorError
        self._numerator = new_numerator
        self._denominator = new_denominator
        self.normalize()

    def __add__(self, other):
        first_numerator = self.numerator
        second_numerator = other.numerator
        first_denominator = self.denominator
        second_denominator = other.denominator
        sum_numerator = (
            first_numerator * second_denominator
            + second_numerator * first_denominator
        )
        sum_denominator = first_denominator * second_denominator
        return Fraction(sum_numerator, sum_denominator)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def add_integer(self, integer):
        pass

    def give_real_value():
        pass

    def __str__(self):
        pass
