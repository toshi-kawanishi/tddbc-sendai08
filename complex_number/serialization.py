class ComplexNumberSerializer(object):
    pass


class DefaultPurelyImaginaryNumberStringSerializer(ComplexNumberSerializer):

    OMITTING_TARGETS = [1, -1]
    IMAGINARY_UNIT = "i"

    @classmethod
    def serialize(cls, number):
        return cls._format_imaginary_part(number.imaginary_part())

    @classmethod
    def _format_imaginary_part(cls, imaginary_part: int) -> str:
        if imaginary_part in cls.OMITTING_TARGETS:
            return f"{cls._short_sign(imaginary_part)}{cls.IMAGINARY_UNIT}"
        else:
            return f"{imaginary_part}{cls.IMAGINARY_UNIT}"

    @staticmethod
    def _short_sign(number: int) -> str:
        if number < 0:
            return "-"
        else:
            return ""
