from typing import Any

from complex_number.serialization import DefaultImaginaryNumberStringSerializer
from complex_number.normalization import IntegerNormalizer, NonZeroIntegerNormalizer


class ComplexNumber(object):
    pass


class RealNumber(ComplexNumber):
    pass


class ImaginaryNumber(ComplexNumber):

    class Normalizers:
        REAL_PART = IntegerNormalizer
        IMAGINARY_PART = NonZeroIntegerNormalizer

    def __init__(self, real_part: int, imaginary_part: int,
                 string_serializer=DefaultImaginaryNumberStringSerializer):
        self._real_part = real_part
        self._imaginary_part = imaginary_part
        self._string_serializer = string_serializer

    def __setattr__(self, name: str, value: Any):
        if name == '_real_part':
            self.__dict__[name] = type(self).Normalizers.REAL_PART.normalize(value)
        elif name == '_imaginary_part':
            self.__dict__[name] = type(self).Normalizers.IMAGINARY_PART.normalize(value)
        else:
            self.__dict__[name] = value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.real_part() == other.real_part() and self.imaginary_part() == other.imaginary_part()
        else:
            return TypeUtils.number_with_exact_type(other) == TypeUtils.number_with_exact_type(self)

    def __str__(self):
        return self._string_serializer.serialize(self)

    def real_part(self) -> int:
        return self._real_part

    def imaginary_part(self) -> int:
        return self._imaginary_part

    def conjugate(self):
        return ImaginaryNumber(self.real_part(), -1 * self.imaginary_part())


class PurelyImaginaryNumber(ImaginaryNumber):

    class Normalizers:
        IMAGINARY_PART = NonZeroIntegerNormalizer

    def __init__(self, imaginary_part: int,
                 string_serializer=DefaultImaginaryNumberStringSerializer):
        super(type(self), self).__init__(None, imaginary_part, string_serializer)

    def __setattr__(self, name: str, value: Any):
        if name == '_real_part':
            pass
        elif name == '_imaginary_part':
            self.__dict__[name] = type(self).Normalizers.IMAGINARY_PART.normalize(value)
        else:
            self.__dict__[name] = value

    def real_part(self):
        return None

    def conjugate(self):
        return PurelyImaginaryNumber(-1 * self.imaginary_part())


class TypeUtils(object):

    @staticmethod
    def exact_type(number: ImaginaryNumber):
        if number.real_part() is None or number.real_part() == 0:
            return PurelyImaginaryNumber
        else:
            return number

    @classmethod
    def number_with_exact_type(cls, number: ImaginaryNumber):
        new_type = cls.exact_type(number)

        if new_type == PurelyImaginaryNumber:
            return PurelyImaginaryNumber(number.imaginary_part())
        else:
            return number
