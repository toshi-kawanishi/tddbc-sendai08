from typing import Any

from complex_number.formatter import DefaultPurelyImaginaryNumberFormatter
from complex_number.validator import ImaginaryPartValidator


class ComplexNumber(object):
    pass


class RealNumber(ComplexNumber):
    pass


class ImaginaryNumber(ComplexNumber):
    pass


class PurelyImaginaryNumber(ImaginaryNumber):

    class Validators:
        IMAGINARY_PART = ImaginaryPartValidator

    def __new__(cls, imaginary_part: int, formatter=DefaultPurelyImaginaryNumberFormatter):
        if not cls.Validators.IMAGINARY_PART.validate(imaginary_part):
            raise ValueError(f"{imaginary_part}は虚部として使用できません")

        return super().__new__(cls)

    def __init__(self, imaginary_part: int, formatter=DefaultPurelyImaginaryNumberFormatter):
        self._imaginary_part = imaginary_part
        self._formatter = formatter

    def __str__(self):
        return self._formatter.format(self)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self.imaginary_part() == other.imaginary_part()

    def imaginary_part(self) -> int:
        return self._imaginary_part

    def conjugate(self):
        return PurelyImaginaryNumber(-1 * self.imaginary_part())
