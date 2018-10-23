class Functions:

    @staticmethod
    def simple_sign(number: int) -> str:
        if number < 0:
            return "-"
        else:
            return ""

    @staticmethod
    def verbose_sign(number: int) -> str:
        if number < 0:
            return "-"
        elif number == 0:
            return "±"
        else:
            return "+"


class ComplexNumberSerializer(object):
    pass


class DefaultImaginaryNumberStringSerializer(ComplexNumberSerializer):

    OMITTING_TARGETS = [1, -1]
    IMAGINARY_UNIT = "i"

    @classmethod
    def serialize(cls, number):
        if number.real_part():
            return "%s %s" % (
                cls._format_real_part(number.real_part()),
                cls._format_imaginary_part(number.imaginary_part(), verbose=True)
            )
        else:
            return cls._format_imaginary_part(number.imaginary_part())

    @classmethod
    def _format_real_part(cls, real_part: int) -> str:
        return str(real_part)

    @classmethod
    def _format_imaginary_part(cls, imaginary_part: int, verbose=False) -> str:
        if verbose:
            sign = Functions.verbose_sign
            margin = ' '
        else:
            sign = Functions.simple_sign
            margin = ''

        if imaginary_part in cls.OMITTING_TARGETS:
            return f"{sign(imaginary_part)}{margin}{cls.IMAGINARY_UNIT}"
        else:
            return f"{sign(imaginary_part)}{margin}{abs(imaginary_part)}{cls.IMAGINARY_UNIT}"
