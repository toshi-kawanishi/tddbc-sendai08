from typing import Any

from complex_number.serialize import DefaultPurelyImaginaryNumberStringSerializer
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

    def __init__(self, imaginary_part: int, string_serializer=DefaultPurelyImaginaryNumberStringSerializer):
        self._imaginary_part = imaginary_part
        self._string_serializer = string_serializer

    def __str__(self):
        return self._string_serializer.serialize(self)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self.imaginary_part() == other.imaginary_part()

    def imaginary_part(self) -> int:
        return self._imaginary_part

    def conjugate(self):
        return PurelyImaginaryNumber(-1 * self.imaginary_part())
