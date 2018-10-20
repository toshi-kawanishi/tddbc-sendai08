class ComplexNumberComponentValidator(object):
    pass


class ImaginaryPartValidator(ComplexNumberComponentValidator):

    @classmethod
    def validate(cls, imaginary_part: int):
        return cls._validate_non_zero(imaginary_part)

    @staticmethod
    def _validate_non_zero(target):
        return target != 0
