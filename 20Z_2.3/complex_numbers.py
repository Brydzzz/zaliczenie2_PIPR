from math import sqrt


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self._real_part = real_part
        self._imaginary_part = imaginary_part

    @property
    def real_part(self):
        """
        Returns complex number real part
        """
        return self._real_part

    @property
    def imaginary_part(self):
        """
        Returns complex number imaginary part
        """
        return self._imaginary_part

    def __add__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        new_real_part = a + c
        new_imaginary_part = b + d
        return ComplexNumber(new_real_part, new_imaginary_part)

    def __sub__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        new_real_part = a - c
        new_imaginary_part = b - d
        return ComplexNumber(new_real_part, new_imaginary_part)

    def __mul__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        new_real_part = a * c - b * d
        new_imaginary_part = a * d + b * c
        return ComplexNumber(new_real_part, new_imaginary_part)

    def __truediv__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        new_real_part = (a * c + b * d) / (c**2 + d**2)
        new_imaginary_part = (b * c - a * d) / (c**2 + d**2)
        return ComplexNumber(new_real_part, new_imaginary_part)

    def __str__(self):
        operator = "+" if self.imaginary_part >= 0 else "-"
        return f"{self.real_part} {operator} {abs(self.imaginary_part)}i"

    def conjugate(self):
        """
        Returns conjugate of complex number
        """
        new_imaginary_part = self.imaginary_part * (-1)
        return ComplexNumber(self.real_part, new_imaginary_part)

    def modulus(self):
        """
        Returns modulus of complex number
        """
        a = self.real_part
        b = self.imaginary_part
        return sqrt(a**2 + b**2)
