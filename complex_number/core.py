from typing import Any

from complex_number.serialize import DefaultPurelyImaginaryNumberStringSerializer
from complex_number.normalize import NonZeroIntegerNormalizer


class ComplexNumber(object):
    pass


class RealNumber(ComplexNumber):
    pass


class ImaginaryNumber(ComplexNumber):
    pass


class PurelyImaginaryNumber(ImaginaryNumber):

    class Normalizers:
        IMAGINARY_PART = NonZeroIntegerNormalizer

    def __init__(self, imaginary_part: int, string_serializer=DefaultPurelyImaginaryNumberStringSerializer):
        self._imaginary_part = imaginary_part
        self._string_serializer = string_serializer

    def __setattr__(self, name: str, value: Any):
        if name == '_imaginary_part':
            self.__dict__[name] = type(self).Normalizers.IMAGINARY_PART.normalize(value)
        else:
            self.__dict__[name] = value

    def __str__(self):
        return self._string_serializer.serialize(self)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, type(self)) and self.imaginary_part() == other.imaginary_part()

    def imaginary_part(self) -> int:
        return self._imaginary_part

    def conjugate(self):
        return PurelyImaginaryNumber(-1 * self.imaginary_part())
