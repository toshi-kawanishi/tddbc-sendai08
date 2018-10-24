from typing import Any, Callable


class Decorators:

    @staticmethod
    def to_int(f: Callable) -> Callable[[Any], int]:
        def decorator(value: Any) -> int:
            return f(int(value))

        return decorator

    @staticmethod
    def check_non_zero(f: Callable) -> Callable[[int], int]:
        def decorator(value: int) -> int:
            if value == 0:
                raise ValueError(f"{value} is zero")
            return f(value)

        return decorator


class ComplexNumberAttributeNormalizer(object):
    pass


class NonZeroIntegerNormalizer(ComplexNumberAttributeNormalizer):

    @staticmethod
    @Decorators.to_int
    @Decorators.check_non_zero
    def normalize(value: Any):
        return value


class IntegerNormalizer(object):

    @staticmethod
    @Decorators.to_int
    def normalize(value: Any):
        return value
